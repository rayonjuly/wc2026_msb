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
    selected_team = st.selectbox('Filter by Team:', dropdown_options)

    df = pd.read_csv(r"standing.csv").dropna(how='all')

    if selected_team != "All Teams":
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
    

    def style_rows(row):
        # Apply a light gray/blue background for even rows, white for odd rows
        bg_color = 'background-color: #f8fafc;' if row.name % 2 == 0 else 'background-color: #ffffff;'
        return [bg_color] * len(row)
    
    dynamic_height = min(len(display_df) * 35 + 40, 1000) 
    display_df = display_df.style.apply(style_rows, axis=1).set_properties(
        subset=['total_score','score_1', 'score_2', 'score_3', 'score_4'], 
        **{'font-weight': 'bold'}
    )

    st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)

    
    # st.caption("Lưu ý: Việc xếp hạng mới tính trên tổng điểm, chưa tính đến các chỉ số phụ. Có thể thay đổi phụ thuộc vào d/s các đội vào vòng 32_team")

with tab_bracket:
    st.subheader("Tournament Bracket")
    st.info("Your bracket code goes here.")