import streamlit as st
import pandas as pd

st.set_page_config(page_title="WC 2026 Ticket Standing", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026")

tab_leaderboard, tab_bracket = st.tabs(["📊 Bảng xếp hạng", "🏟️ Nhánh đấu"])

with tab_leaderboard:
    # st.subheader("Bảng xếp hạng chính thức tính đến 10h00 ngày 2026-06-25")
    
    # Load the full dataset from your CSV file
    # Make sure 'leaderboard_data.csv' is saved in the same folder as this Python script

    df_dim_team = pd.read_csv('dim_team.csv')
    dim_team = df_dim_team['team'].tolist()

    dropdown_options = ['All Teams'] + dim_team
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
    st.subheader("Bảng đấu (Tournament Bracket)")
    
    # 1. CSS for the bracket boxes (updated without pot labels)
    st.markdown("""
    <style>
        .team-box {
            padding: 8px 4px;
            margin: 4px 0;
            border-radius: 4px;
            background-color: #1e293b;
            color: #e2e8f0;
            border: 1px solid #334155;
            text-align: center;
            font-size: 13px;
            font-weight: 500;
            height: 38px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }
        .highlighted {
            background-color: #1d4ed8 !important; /* Strong Blue */
            color: white !important;
            border: 2px solid #60a5fa !important; /* Light blue border */
            box-shadow: 0 0 8px rgba(96, 165, 250, 0.6);
            font-weight: bold;
        }
        .round-title {
            text-align: center;
            font-weight: bold;
            color: #94a3b8;
            font-size: 14px;
            margin-bottom: 10px;
        }
        .spacer {
            /* Helper class for vertical alignment */
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. Mock Data for demonstration
    # In your real app, this list comes from the user selecting a ticket in the dropdown
    selected_ticket_teams = ["Germany", "France", "Brazil", "Argentina", "Canada"]
    
    # In your real app, this mapping comes from your dataset determining who advanced
    # We set Canada and Germany to 16_team to test the highlight logic!
    team_current_rounds = {
        "Germany": "16_team", "Japan": "32_team",
        "France": "32_team", "Scotland": "32_team",
        "Brazil": "32_team", "Netherlands": "32_team",
        "Argentina": "32_team", "Uruguay": "32_team",
        "Canada": "16_team", "Algeria": "32_team",
        # Assume all others are 32_team for this example
    }

    # 3. The Smart Render Function
    def render_team(team_name, column_round, ticket_teams, current_rounds):
        # Default to 32_team if the team isn't in our dictionary yet
        actual_round = current_rounds.get(team_name, "32_team")
        
        # LOGIC: Highlight ONLY IF the team is in the ticket AND this block matches their current round
        is_highlighted = ""
        if (team_name in ticket_teams) and (actual_round == column_round):
            is_highlighted = "highlighted"
            
        st.markdown(f"""
            <div class="team-box {is_highlighted}">
                {team_name}
            </div>
        """, unsafe_allow_html=True)

    # 4. Bracket Layout Data (Extracted from your image)
    left_r32 = [
        ("Germany", "Japan"), ("France", "Scotland"), 
        ("South Korea", "Switzerland"), ("Sweden", "Morocco"),
        ("Portugal", "Croatia"), ("Spain", "Austria"),
        ("USA", "Bosnia and Herzegovina"), ("Belgium", "Ecuador")
    ]
    
    right_r32 = [
        ("Brazil", "Netherlands"), ("Ivory Coast", "Norway"),
        ("Mexico", "Senegal"), ("England", "DR Congo"),
        ("Argentina", "Uruguay"), ("Australia", "Egypt"),
        ("Canada", "Algeria"), ("Colombia", "Turkiye")
    ]

    # 5. Build the Columns
    c_l_32, c_l_16, c_l_qf, c_center, c_r_qf, c_r_16, c_r_32 = st.columns([1.5, 1.2, 1.2, 1, 1.2, 1.2, 1.5])

    # --- LEFT WING ---
    with c_l_32:
        st.markdown("<div class='round-title'>R32</div>", unsafe_allow_html=True)
        for match in left_r32:
            render_team(match[0], "32_team", selected_ticket_teams, team_current_rounds)
            render_team(match[1], "32_team", selected_ticket_teams, team_current_rounds)
            st.write("") # Gap between matches

    with c_l_16:
        st.markdown("<div class='round-title'>R16</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
        # Mocking the R16 advanced teams
        render_team("Germany", "16_team", selected_ticket_teams, team_current_rounds)
        st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
        render_team("France", "16_team", selected_ticket_teams, team_current_rounds)
        # Add more spacers and render_team calls as teams advance...

    with c_l_qf:
        st.markdown("<div class='round-title'>QF</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        render_team("TBD", "quarter_final", selected_ticket_teams, team_current_rounds)

    # --- CENTER ---
    with c_center:
        st.markdown("<div class='round-title'>Final</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        render_team("TBD", "final", selected_ticket_teams, team_current_rounds)

    # --- RIGHT WING ---
    with c_r_qf:
        st.markdown("<div class='round-title'>QF</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        render_team("TBD", "quarter_final", selected_ticket_teams, team_current_rounds)

    with c_r_16:
        st.markdown("<div class='round-title'>R16</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
        render_team("Brazil", "16_team", selected_ticket_teams, team_current_rounds)
        st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
        render_team("Canada", "16_team", selected_ticket_teams, team_current_rounds)

    with c_r_32:
        st.markdown("<div class='round-title'>R32</div>", unsafe_allow_html=True)
        for match in right_r32:
            render_team(match[0], "32_team", selected_ticket_teams, team_current_rounds)
            render_team(match[1], "32_team", selected_ticket_teams, team_current_rounds)
            st.write("") # Gap between matches