import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode

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
    dim_user = df['ticket'].str.split(" - ").str[0].drop_duplicates().sort_values(key=lambda col: col.apply(unidecode)).tolist()
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
ticket_list = df['ticket'].drop_duplicates().sort_values(key=lambda col: col.apply(unidecode)).tolist()

with tab_bracket:

    selected_ticket = st.selectbox("Lọc theo vé:", ticket_list)
    
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


    team_data = pd.read_csv('fact_current_round.csv').set_index('team').to_dict(orient='index')

    # 3. Dynamic Highlighting Function
    def get_team_box(team_name, render_round):
        box_class = "team"
        
        # Only process highlights if the team is in the selected ticket
        if team_name in selected_teams:
            info = team_data.get(team_name, {})
            actual_round = info.get('current_round', '32_team')
            status = info.get('team_status', 1)
            
            # THE FIX: Only apply colors if the column we are drawing matches their current highest round!
            if actual_round == render_round:
                if status == 1:
                    box_class += " highlight-green"
                else:
                    box_class += " highlight-red"
                    
        return f'<div class="{box_class}">{team_name}</div>'

    # 4. HTML & CSS for the Bracket layout (Fixed Arguments & Added Semi-Finals)
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
        /* NEW: Wrapper to hold headers and the bracket together */
        .tournament-wrapper {{
            min-width: 1400px;
            # background-color: #0f172a;
            background-color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
        }}
        
        /* NEW: Header layout */
        .tournament-headers {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }}
        .round-title {{
            color: #ef4444; /* Red color matching your image */
            text-align: center;
            font-weight: bold;
            font-size: 14px;
        }}
        .tournament-container {{
            display: flex;
            justify-content: space-between;
            align-items: stretch;
            width: 100%;
            min-width: 1400px; /* Widened to fit the extra SF columns */
            padding: 20px;
            background-color: #0f172a;
            border-radius: 10px;
        }}
        .col {{
            display: flex;
            flex-direction: column;
            justify-content: space-around;
        }}
        .col-teams {{ width: 120px; gap: 8px; }}
        .col-paths {{ width: 25px; }}
        
        .match {{
            display: flex;
            flex-direction: column;
            gap: 2px;
            margin: 4px 0;
        }}
        .team {{
            background-color: #1e293b;
            border: 1px solid #d4af37;
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
        
        .highlight-green {{
            background-color: #166534 !important;
            border: 2px solid #4ade80 !important;
            color: white;
            box-shadow: 0 0 10px rgba(74, 222, 128, 0.6);
        }}
        .highlight-red {{
            background-color: #991b1b !important;
            border: 2px solid #f87171 !important;
            color: white;
            text-decoration: line-through;
            opacity: 0.8;
        }}

        .path-left {{
            border-top: 2px solid #3b82f6;
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
        /* NEW: Straight line for SF to Final */
        .path-straight {{
            border-bottom: 2px solid #3b82f6;
            width: 100%;
            height: 50%;
        }}
        /* Heights for dynamic spanning */
        .h-r32 {{ height: 50px; }}
        .h-r16 {{ height: 110px; }}
        .h-qf {{ height: 235px; }}
        .h-sf {{ height: 480px; }} /* THE NEW SF LINE HEIGHT */
        
        .center-stage {{
            display: flex;
            flex-direction: column;
            justify-content: center; /* Perfectly centers the final match vertically */
            align-items: center;
            width: 160px;
            position: relative; /* Allows trophy to float */
        }}
        .trophy-space {{ height: 60px; text-align: center; font-size: 20px; color: gold; font-weight: bold; margin-bottom: 20px; }}
    </style>
    </head>
    <body>
        <div class="tournament-wrapper">
            
            <div class="tournament-headers">
                <div class="col-teams round-title">32 ĐỘI</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">16 ĐỘI</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">TỨ KẾT</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">BÁN KẾT</div>
                <div class="col-paths"></div>
                <div class="center-stage round-title" style="margin-bottom: 0;">CHUNG KẾT</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">BÁN KẾT</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">TỨ KẾT</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">16 ĐỘI</div>
                <div class="col-paths"></div>
                <div class="col-teams round-title">32 ĐỘI</div>
            </div>

            <div class="tournament-container">
                
                <div class="col col-teams">
                    <div class="match">{get_team_box("Germany", "32_team")}{get_team_box("Paraguay", "32_team")}</div>
                    <div class="match">{get_team_box("France", "32_team")}{get_team_box("Sweden", "32_team")}</div>
                    <div class="match">{get_team_box("South Africa", "32_team")}{get_team_box("Canada", "32_team")}</div>
                    <div class="match">{get_team_box("Netherlands", "32_team")}{get_team_box("Morocco", "32_team")}</div>
                    <div class="match">{get_team_box("Portugal", "32_team")}{get_team_box("Croatia", "32_team")}</div>
                    <div class="match">{get_team_box("Spain", "32_team")}{get_team_box("Austria", "32_team")}</div>
                    <div class="match">{get_team_box("USA", "32_team")}{get_team_box("Bosnia and Herzegovina", "32_team")}</div>
                    <div class="match">{get_team_box("Belgium", "32_team")}{get_team_box("Senegal", "32_team")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-left h-r32"></div><div class="path-left h-r32"></div>
                    <div class="path-left h-r32"></div><div class="path-left h-r32"></div>
                </div>

                <div class="col col-teams" style="justify-content: space-around; padding: 20px 0;">
                    <div class="match">{get_team_box("Paraguay", "16_team")}{get_team_box("France", "16_team")}</div>
                    <div class="match">{get_team_box("Canada", "16_team")}{get_team_box("Morocco", "16_team")}</div>
                    <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                    <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-left h-r16"></div><div class="path-left h-r16"></div>
                </div>

                <div class="col col-teams" style="justify-content: space-around; padding: 80px 0;">
                    <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                    <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-left h-qf"></div>
                </div>
                
                <div class="col col-teams" style="justify-content: center;">
                    <div class="match">{get_team_box("TBD", "semi_final")}{get_team_box("TBD", "semi_final")}</div>
                </div>

                <div class="center-stage">
                    <div class="trophy-space">🏆 CHAMPION</div>
                    <div class="match" style="width: 140px;">
                        {get_team_box("FINALIST 1", "final")}
                        {get_team_box("FINALIST 2", "final")}
                    </div>
                </div>
                
                <div class="col col-teams" style="justify-content: center;">
                    <div class="match">{get_team_box("TBD", "semi_final")}{get_team_box("TBD", "semi_final")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-right h-qf"></div>
                </div>

                <div class="col col-teams" style="justify-content: space-around; padding: 80px 0;">
                    <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                    <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-right h-r16"></div><div class="path-right h-r16"></div>
                </div>

                <div class="col col-teams" style="justify-content: space-around; padding: 20px 0;">
                    <div class="match">{get_team_box("Brazil", "16_team")}{get_team_box("Norway", "16_team")}</div>
                    <div class="match">{get_team_box("Mexico", "16_team")}{get_team_box("TBD", "16_team")}</div>
                    <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                    <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                </div>

                <div class="col col-paths">
                    <div class="path-right h-r32"></div><div class="path-right h-r32"></div>
                    <div class="path-right h-r32"></div><div class="path-right h-r32"></div>
                </div>

                <div class="col col-teams">
                    <div class="match">{get_team_box("Brazil", "32_team")}{get_team_box("Japan", "32_team")}</div>
                    <div class="match">{get_team_box("Ivory Coast", "32_team")}{get_team_box("Norway", "32_team")}</div>
                    <div class="match">{get_team_box("Mexico", "32_team")}{get_team_box("Ecuador", "32_team")}</div>
                    <div class="match">{get_team_box("England", "32_team")}{get_team_box("DR Congo", "32_team")}</div>
                    <div class="match">{get_team_box("Argentina", "32_team")}{get_team_box("Cape Verde", "32_team")}</div>
                    <div class="match">{get_team_box("Australia", "32_team")}{get_team_box("Egypt", "32_team")}</div>
                    <div class="match">{get_team_box("Switzerland", "32_team")}{get_team_box("Algeria", "32_team")}</div>
                    <div class="match">{get_team_box("Colombia", "32_team")}{get_team_box("Ghana", "32_team")}</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # 5. Render the custom HTML
    components.html(bracket_html, height=800, scrolling=True)