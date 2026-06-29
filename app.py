import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="WC 2026 Ticket Standing", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026")

# tab_leaderboard, tab_bracket = st.tabs(["📊 Bảng xếp hạng", "🏟️ Nhánh đấu"])

tab_leaderboard = st.tabs(["📊 Bảng xếp hạng"])

with tab_leaderboard:
    # st.subheader("Bảng xếp hạng chính thức tính đến 10h00 ngày 2026-06-25")
    
    # Load the full dataset from your CSV file
    # Make sure 'leaderboard_data.csv' is saved in the same folder as this Python script

    df_dim_team = pd.read_csv('dim_team.csv')
    dim_team = df_dim_team['team'].tolist()

    dropdown_options = ['Tất cả'] + dim_team
    selected_team = st.selectbox('Lọc theo đội:', dropdown_options)

    df = pd.read_csv(r"standing.csv").dropna(how='all')

    if selected_team != "Tất cả":
        # Create a filter mask that checks if the selected team is in ANY of the 4 columns
        mask = (df['team_1'].str.contains(selected_team)) | \
                (df['team_2'].str.contains(selected_team)) | \
                (df['team_3'].str.contains(selected_team)) | \
                (df['team_4'].str.contains(selected_team))
        
        # Apply the mask to get the filtered data
        display_df = df[mask]
    else:
        # If "All Teams" is selected, show everything
        display_df = df
    

    # def style_rows(row):
    #     # Apply a light gray/blue background for even rows, white for odd rows
    #     bg_color = 'background-color: #f8fafc;' if row.name % 2 == 0 else 'background-color: #ffffff;'
    #     return [bg_color] * len(row)
    
    dynamic_height = min(len(display_df) * 35 + 40, 1000) 
    display_df = display_df.style.set_properties(
        subset=['total_score','score_1', 'score_2', 'score_3', 'score_4'], 
        **{'font-weight': 'bold'}
    )

    st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)

    
    # st.caption("Lưu ý: Việc xếp hạng mới tính trên tổng điểm, chưa tính đến các chỉ số phụ. Có thể thay đổi phụ thuộc vào d/s các đội vào vòng 32_team")

with tab_bracket:
    st.subheader("🏆 Knockouts (Tournament Bracket)")
    
    # 1. Mock Data (Replace with your actual dynamic variables)
    selected_ticket_teams = ["Germany", "France", "Brazil", "Argentina", "Canada"]
    
    # Current rounds mapping (Canada and Germany set to 16_team to test highlighting!)
    team_current_rounds = {
        "Germany": "16_team", "France": "16_team", 
        "Brazil": "16_team", "Argentina": "32_team",
        "Canada": "16_team"
    }

    # 2. Python function to generate the HTML for a single team box
    def get_team_box(team_name, round_name):
        actual_round = team_current_rounds.get(team_name, "32_team")
        # Logic: Highlight ONLY if in ticket AND the rendered round matches their current furthest round
        is_highlighted = "highlight" if (team_name in selected_ticket_teams) and (actual_round == round_name) else ""
        return f'<div class="team {is_highlighted}">{team_name}</div>'

    # 3. Build the HTML String
    # We use CSS flexbox to create the columns and CSS borders to draw the connecting paths!
    bracket_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: transparent;
            color: #f8fafc;
            margin: 0;
        }}
        .tournament-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            min-width: 1000px; /* Forces scrolling on small screens */
            padding: 10px;
        }}
        .col {{
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            height: 800px; /* Fixed height to align paths */
        }}
        .col-teams {{ width: 140px; }}
        .col-paths {{ width: 30px; }}
        
        /* Team Box Styling */
        .match {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .team {{
            background-color: #1e293b;
            border: 1px solid #334155;
            padding: 6px;
            font-size: 11px;
            text-align: center;
            border-radius: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            transition: all 0.2s ease;
        }}
        .highlight {{
            background-color: #1d4ed8 !important;
            border-color: #60a5fa !important;
            font-weight: bold;
            color: white;
            box-shadow: 0 0 10px rgba(96, 165, 250, 0.6);
        }}
        .round-title {{
            text-align: center;
            font-size: 12px;
            font-weight: bold;
            color: #94a3b8;
            margin-bottom: 10px;
        }}

        /* Connecting Path Lines (The Magic) */
        .path-left {{
            border-top: 2px solid #475569;
            border-right: 2px solid #475569;
            border-bottom: 2px solid #475569;
            border-left: none;
            border-radius: 0 6px 6px 0;
            margin: auto 0;
        }}
        .path-right {{
            border-top: 2px solid #475569;
            border-left: 2px solid #475569;
            border-bottom: 2px solid #475569;
            border-right: none;
            border-radius: 6px 0 0 6px;
            margin: auto 0;
        }}
        /* Heights for the connecting lines spanning between matches */
        .h-r32 {{ height: 75px; }}
        .h-r16 {{ height: 180px; }}
        .h-qf {{ height: 380px; }}
    </style>
    </head>
    <body>
        <div class="tournament-container">
            
            <div class="col col-teams">
                <div class="round-title">R32</div>
                <div class="match">{get_team_box("Germany", "32_team")}{get_team_box("Paraguay", "32_team")}</div>
                <div class="match">{get_team_box("France", "32_team")}{get_team_box("Sweden", "32_team")}</div>
                <div class="match">{get_team_box("South Africa", "32_team")}{get_team_box("Canada", "32_team")}</div>
                <div class="match">{get_team_box("Netherlands", "32_team")}{get_team_box("Morocco", "32_team")}</div>
                <div class="match">{get_team_box("RU Grp K", "32_team")}{get_team_box("RU Grp L", "32_team")}</div>
                <div class="match">{get_team_box("Spain", "32_team")}{get_team_box("RU Grp J", "32_team")}</div>
                <div class="match">{get_team_box("USA", "32_team")}{get_team_box("Bosnia & Herz", "32_team")}</div>
                <div class="match">{get_team_box("Belgium", "32_team")}{get_team_box("3rd Grp A/I", "32_team")}</div>
            </div>

            <div class="col col-paths">
                <div style="height: 25px;"></div>
                <div class="path-left h-r32"></div>
                <div class="path-left h-r32"></div>
                <div class="path-left h-r32"></div>
                <div class="path-left h-r32"></div>
            </div>

            <div class="col col-teams">
                <div class="round-title">R16</div>
                <div class="match">{get_team_box("Germany", "16_team")}{get_team_box("France", "16_team")}</div>
                <div class="match">{get_team_box("Canada", "16_team")}{get_team_box("TBD", "16_team")}</div>
                <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-left h-r16"></div>
                <div class="path-left h-r16"></div>
            </div>

            <div class="col col-teams">
                <div class="round-title">1/4 Finals</div>
                <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-left h-qf"></div>
            </div>

            <div class="col col-teams" style="width: 160px; justify-content: center; gap: 40px;">
                <div>
                    <div class="round-title">1/2 Finals</div>
                    <div class="match">{get_team_box("TBD", "semi_final")}</div>
                </div>
                <div>
                    <div class="round-title" style="color: #fde047; font-size: 16px;">FINAL</div>
                    <div class="match">
                        {get_team_box("TBD (Left)", "final")}
                        {get_team_box("TBD (Right)", "final")}
                    </div>
                </div>
                <div>
                    <div class="round-title">1/2 Finals</div>
                    <div class="match">{get_team_box("TBD", "semi_final")}</div>
                </div>
            </div>

            <div class="col col-paths">
                <div class="path-right h-qf"></div>
            </div>

            <div class="col col-teams">
                <div class="round-title">1/4 Finals</div>
                <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
                <div class="match">{get_team_box("TBD", "quarter_final")}{get_team_box("TBD", "quarter_final")}</div>
            </div>

            <div class="col col-paths">
                <div class="path-right h-r16"></div>
                <div class="path-right h-r16"></div>
            </div>

            <div class="col col-teams">
                <div class="round-title">R16</div>
                <div class="match">{get_team_box("Brazil", "16_team")}{get_team_box("TBD", "16_team")}</div>
                <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
                <div class="match">{get_team_box("TBD", "16_team")}{get_team_box("TBD", "16_team")}</div>
            </div>

            <div class="col col-paths">
                <div style="height: 25px;"></div>
                <div class="path-right h-r32"></div>
                <div class="path-right h-r32"></div>
                <div class="path-right h-r32"></div>
                <div class="path-right h-r32"></div>
            </div>

            <div class="col col-teams">
                <div class="round-title">R32</div>
                <div class="match">{get_team_box("Brazil", "32_team")}{get_team_box("Japan", "32_team")}</div>
                <div class="match">{get_team_box("Ivory Coast", "32_team")}{get_team_box("Norway", "32_team")}</div>
                <div class="match">{get_team_box("Mexico", "32_team")}{get_team_box("3rd Grp C/E", "32_team")}</div>
                <div class="match">{get_team_box("Win Grp L", "32_team")}{get_team_box("3rd Grp I/J/K", "32_team")}</div>
                <div class="match">{get_team_box("Argentina", "32_team")}{get_team_box("Cape Verde", "32_team")}</div>
                <div class="match">{get_team_box("Australia", "32_team")}{get_team_box("Egypt", "32_team")}</div>
                <div class="match">{get_team_box("Switzerland", "32_team")}{get_team_box("3rd Grp G/J", "32_team")}</div>
                <div class="match">{get_team_box("Win Grp K", "32_team")}{get_team_box("3rd Grp E/H/I", "32_team")}</div>
            </div>

        </div>
    </body>
    </html>
    """

    # 4. Render the HTML in Streamlit
    components.html(bracket_html, height=850, scrolling=True)