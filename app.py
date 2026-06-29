import streamlit as st
import pandas as pd

st.set_page_config(page_title="WC 2026 Ticket Standing", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026")

tab_leaderboard, tab_bracket = st.tabs(["📊 Bảng xếp hạng", "🏟️ Nhánh đấu"])

with tab_leaderboard:
    # st.subheader("Bảng xếp hạng chính thức tính đến 10h00 ngày 2026-06-25")
    
    # Load the full dataset from your CSV file
    # Make sure 'leaderboard_data.csv' is saved in the same folder as this Python script

    df = pd.read_csv(r"standing.csv")
    
    # Display the entire dataframe
    # use_container_width=True makes it stretch across the screen
    st.dataframe(df, use_container_width=True, hide_index=True, height=1000)
        
    
    # st.caption("Lưu ý: Việc xếp hạng mới tính trên tổng điểm, chưa tính đến các chỉ số phụ. Có thể thay đổi phụ thuộc vào d/s các đội vào vòng 32_team")

with tab_bracket:
    st.subheader("Tournament Bracket")
    st.info("Your bracket code goes here.")