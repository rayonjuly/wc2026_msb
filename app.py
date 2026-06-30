import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")

# tab_leaderboard, tab_bracket = st.tabs(["📊 Bảng xếp hạng", "🏟️ Nhánh đấu"])

# tab_leaderboard = st.tabs(["📊 Bảng xếp hạng"])

# with tab_leaderboard:
st.caption("Cập nhật đến sau trận đấu Germany - Paraguay")
    
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


display_df = display_df.rename({
    'rank': 'Vị trí'
    ,'ticket': 'Vé'
    ,'total_score': 'Tổng điểm'
    ,'pot_selected': 'Các nhóm hạt giống'
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

display_df = display_df.style.set_properties(
    subset=['Tổng điểm','Điểm team 1', 'Điểm team 2', 'Điểm team 3', 'Điểm team 4'], 
    **{'font-weight': 'bold'}
)

st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)

    
    # st.caption("Lưu ý: Việc xếp hạng mới tính trên tổng điểm, chưa tính đến các chỉ số phụ. Có thể thay đổi phụ thuộc vào d/s các đội vào vòng 32_team")

# with tab_bracket:
    # st.caption("T")