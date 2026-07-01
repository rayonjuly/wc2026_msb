import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")
st.caption("Cập nhật đến sau trận đấu Mexico - Ecuador")

df = pd.read_csv(r"standing.csv").dropna(how='all')



df_dim_team = pd.read_csv('dim_team.csv')
dim_team = df_dim_team['team'].tolist()

dropdown_options = ['Tất cả'] + dim_team
selected_team = st.selectbox('Lọc theo đội:', dropdown_options)



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

display_df = display_df.style.set_properties(
                            subset=score_cols, 
                            **{'font-weight': 'bold'}
                        )



st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)