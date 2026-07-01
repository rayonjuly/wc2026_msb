import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")
st.caption("Cập nhật đến sau trận đấu Mexico - Ecuador")

tab1, tab2, tab_bracket = st.tabs(["Bảng xếp hạng", "Cách tính điểm", "Phân nhánh"])

with tab1:

    # Load data
    df = pd.read_csv(r"standing.csv").dropna(how='all')
    df_dim_team = pd.read_csv('dim_team.csv')

    # Search box: Theo team
    dim_team = df_dim_team['team'].tolist()
    dropdown_team = ['Tất cả'] + dim_team

    col1, col2 = st.columns(2)
    with col1:
        selected_team_1 = st.selectbox('Lọc theo đội 1:', dropdown_team)
    with col2:
        selected_team_2 = st.selectbox('Lọc theo đội 2:', dropdown_team)

    # Search box: Theo người chơi
    dim_user = df['ticket'].str.split(" - ").str[0].str.strip().unique().tolist()
    dropdown_user = ['Tất cả'] + dim_user
    selected_user = st.selectbox('Lọc theo người chơi:', dropdown_user)

    mask_team_1 = pd.Series(True, index=df.index)
    mask_team_2 = pd.Series(True, index=df.index)
    mask_user = pd.Series(True, index=df.index)

    if selected_team_1 != "Tất cả":
        mask_team_1 = (df['team_1'].str.contains(selected_team_1)) | \
                (df['team_2'].str.contains(selected_team_1)) | \
                (df['team_3'].str.contains(selected_team_1)) | \
                (df['team_4'].str.contains(selected_team_1))

    if selected_team_2 != "Tất cả":
        mask_team_2 = (df['team_1'].str.contains(selected_team_2)) | \
                (df['team_2'].str.contains(selected_team_2)) | \
                (df['team_3'].str.contains(selected_team_2)) | \
                (df['team_4'].str.contains(selected_team_2))
        
    if selected_user != "Tất cả":
        mask_user = df['ticket'].str.contains(selected_user)

    mask = mask_team_1 & mask_team_2 & mask_user 
    display_df = df[mask]

    display_df = display_df.rename({
        'rank': 'Vị trí'
        ,'ticket': 'Vé'
        ,'total_score': 'Tổng điểm'
        ,'pot_selected': 'Hạt giống'
        ,'teams_active': 'Số đội còn thi đấu'
        ,'team_1': 'Team 1'
        ,'round_1': 'Vị trí team 1'
        ,'score_1': 'Điểm team 1'
        ,'team_2': 'Team 2'
        ,'round_2': 'Vị trí team 2'
        ,'score_2': 'Điểm team 2'
        ,'team_3': 'Team 3'
        ,'round_3': 'Vị trí team 3'
        ,'score_3': 'Điểm team 3'
        ,'team_4': 'Team 4'
        ,'round_4': 'Vị trí team 4'
        ,'score_4': 'Điểm team 4'
    }, axis=1)

    dynamic_height = min(len(display_df) * 35 + 40, 1000) 
    team_cols = ['Team 1', 'Team 2', 'Team 3', 'Team 4']
    score_cols = ['Tổng điểm','Điểm team 1', 'Điểm team 2', 'Điểm team 3', 'Điểm team 4']

    # highlight teams

    df_fact_current_round = pd.read_csv(r"fact_current_round.csv")
    status_dict = dict(zip(df_fact_current_round['team'], df_fact_current_round['team_status']))

    def highlight_team_status(team_string):
    # If the cell is empty, return no styling
        if pd.isna(team_string):
            return ''
            
        # Clean the string to match the dictionary keys
        # "Spain (pot 1)" becomes "Spain"
        base_team_name = str(team_string).split(' (')[0]
        
        # If the team isn't in our dictionary, return no styling
        if base_team_name not in status_dict:
            return ''
            
        status = status_dict[base_team_name]
        
        # 0 = Eliminated (Light red background, dark red text)
        if status == 0:
            return 'background-color: #fee2e2; color: #991b1b;' 
        # 1 = Active (Light green background, dark green text)
        elif status == 1:
            return 'background-color: #dcfce7; color: #166534;'
            
        return ''

    display_df = display_df \
            .style.map(
                highlight_team_status
                ,subset = team_cols
            ) \
            .set_properties(
                subset=score_cols, 
                **{'font-weight': 'bold'}
            ) 

    
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)

with tab2:
    st.image("Scoring_rule.png")

# status_dict = {'Brazil': 1, 'Japan': 0, 'Spain': 1, 'Mexico': 0, 'Germany': 1, 'Canada': 0}
ticket_list = df['ticket'].drop_duplicates().tolist()

with tab_bracket:
    # st.subheader("🏟️ Bảng Đấu (Tournament Bracket)")
    
    # 1. Dropdown to select a specific ticket to visualize
    selected_ticket = st.selectbox("Lọc theo vé:", ticket_list)
    
    # 2. Extract the base team names for the selected ticket
    # (Assuming your dataframe 'df' has columns team_1, team_2, team_3, team_4)
    # We use a try/except here just in case the ticket isn't found perfectly
    selected_teams = []
    try:
        # Get the row for the selected ticket
        ticket_row = df[df['ticket'] == selected_ticket].iloc[0]
        # Extract base names (removes the " (pot X)" part)
        selected_teams = [
            str(ticket_row['team_1']).split(' (')[0],
            str(ticket_row['team_2']).split(' (')[0],
            str(ticket_row['team_3']).split(' (')[0],
            str(ticket_row['team_4']).split(' (')[0]
        ]
    except Exception as e:
        # Fallback for testing if df isn't linked correctly
        selected_teams = ['Germany', 'Brazil', 'Spain', 'Mexico']

    # 3. Dynamic Highlighting Function
    def get_team_box(team_name):
        # Default classes
        box_class = "team"
        
        if team_name in selected_teams:
            # Check elimination status
            status = status_dict.get(team_name, 1) # Default to 1 if not found
            if status == 1:
                box_class += " highlight-green"
            else:
                box_class += " highlight-red"
                
        return f'<div class="{box_class}">{team_name}</div>'

    # 4. HTML & CSS for the Bracket layout
    bracket_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: transparent;
            color: #e2e8f0;
            margin: 0;
        }}
        .tournament-container {{
            display: flex;
            justify-content: space-between;
            align-items: stretch;
            width: 100%;
            min-width: 1200px; /* Forces scrollbar on small screens */
            padding: 20px;
            background-color: #0f172a; /* Dark background like the image */
            border-radius: 10px;
        }}
        .col {{
            display: flex;
            flex-direction: column;
            justify-content: space-around;
        }}
        .col-teams {{ width: 130px; gap: 8px; }}
        .col-paths {{ width: 30px; }}
        
        .match {{
            display: flex;
            flex-direction: column;
            gap: 2px;
            margin: 4px 0;
        }}
        .team {{
            background-color: #1e293b;
            border: 1px solid #d4af37; /* Gold border */
            color: #f8fafc;
            padding: 4px 6px;
            font-size: 11px;
            font-weight: bold;
            text-align: center;
            border-radius: 3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
            transition: all 0.2s ease;
        }}
        
        /* THE HIGHLIGHT CLASSES */
        .highlight-green {{
            background-color: #166534 !important; /* Dark Green */
            border: 2px solid #4ade80 !important; /* Bright Green Border */
            color: white;
            box-shadow: 0 0 10px rgba(74, 222, 128, 0.6);
        }}
        .highlight-red {{
            background-color: #991b1b !important; /* Dark Red */
            border: 2px solid #f87171 !important; /* Bright Red Border */
            color: white;
            text-decoration: line-through;
            opacity: 0.8;
        }}

        /* Connecting Paths */
        .path-left {{
            border-top: 2px solid #3b82f6; /* Blue lines */
            border-right: 2px solid #3b82f6;
            border-bottom: 2px solid #3b82f6;
            border-radius: 0 4px 4px 0;
            margin: auto 0;
        }}
        .path-right {{
            border-top: 2px solid #3b82f6;
            border-left: 2px solid #3b82f6;
            border-bottom: 2px solid #3b82f6;
            border-radius: 4px 0 0 4px;
            margin: auto 0;
        }}
        .path-center {{
            border-bottom: 2px solid #3b82f6;
            width: 100%;
            height: 50%;
        }}
        
        /* Heights for dynamic spanning */
        .h-r32 {{ height: 50px; }}
        .h-r16 {{ height: 110px; }}
        .h-qf {{ height: 230px; }}
        
        .center-stage {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 200px;
        }}
        .trophy-space {{ height: 100px; text-align: center; font-size: 24px; color: gold; font-weight: bold; margin-bottom: 20px; }}
    </style>
    </head>
    <body>
        <div class="tournament-container">
            
            <div class="col col-teams">
                <div class="match">{get_team_box("Germany")}{get_team_box("Paraguay")}</div>
                <div class="match">{get_team_box("France")}{get_team_box("Sweden")}</div>
                <div class="match">{get_team_box("South Africa")}{get_team_box("Canada")}</div>
                <div class="match">{get_team_box("Netherlands")}{get_team_box("Morocco")}</div>
                <div class="match">{get_team_box("Portugal")}{get_team_box("Croatia")}</div>
                <div class="match">{get_team_box("Spain")}{get_team_box("Austria")}</div>
                <div class="match">{get_team_box("United States")}{get_team_box("Bosnia & Herz.")}</div>
                <div class="match">{get_team_box("Belgium")}{get_team_box("Senegal")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-left h-r32"></div><div class="path-left h-r32"></div>
                <div class="path-left h-r32"></div><div class="path-left h-r32"></div>
            </div>

            <div class="col col-teams" style="justify-content: space-around; padding: 20px 0;">
                <div class="match">{get_team_box("Paraguay")}{get_team_box("France")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-left h-r16"></div><div class="path-left h-r16"></div>
            </div>

            <div class="col col-teams" style="justify-content: space-around; padding: 60px 0;">
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-left h-qf"></div>
            </div>

            <div class="center-stage">
                <div class="trophy-space">🏆 CHAMPION</div>
                <div class="match" style="width: 140px; margin-bottom: 30px;">
                    {get_team_box("FINALIST 1")}
                    {get_team_box("FINALIST 2")}
                </div>
            </div>

            <div class="col col-paths">
                <div class="path-right h-qf"></div>
            </div>

            <div class="col col-teams" style="justify-content: space-around; padding: 60px 0;">
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-right h-r16"></div><div class="path-right h-r16"></div>
            </div>

            <div class="col col-teams" style="justify-content: space-around; padding: 20px 0;">
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
                <div class="match">{get_team_box("TBD")}{get_team_box("TBD")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-right h-r32"></div><div class="path-right h-r32"></div>
                <div class="path-right h-r32"></div><div class="path-right h-r32"></div>
            </div>

            <div class="col col-teams">
                <div class="match">{get_team_box("Brazil")}{get_team_box("Japan")}</div>
                <div class="match">{get_team_box("Ivory Coast")}{get_team_box("Norway")}</div>
                <div class="match">{get_team_box("Mexico")}{get_team_box("Ecuador")}</div>
                <div class="match">{get_team_box("England")}{get_team_box("DR Congo")}</div>
                <div class="match">{get_team_box("Argentina")}{get_team_box("Cape Verde")}</div>
                <div class="match">{get_team_box("Australia")}{get_team_box("Egypt")}</div>
                <div class="match">{get_team_box("Switzerland")}{get_team_box("Algeria")}</div>
                <div class="match">{get_team_box("Colombia")}{get_team_box("Ghana")}</div>
            </div>

        </div>
    </body>
    </html>
    """

    # 5. Render the custom HTML
    components.html(bracket_html, height=750, scrolling=True)