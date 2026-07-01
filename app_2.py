import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")
st.caption("Cập nhật đến sau trận đấu Mexico - Ecuador")

tab1, tab2 = st.tabs(["Bảng xếp hạng", "Cách tính điểm"])

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

    df_fact_current_round = pd.read_csv(r"..\wc2026\data\fact_current_round.csv")
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
            ) \

    
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)

with tab2:
    st.image("Scoring_rule.png")