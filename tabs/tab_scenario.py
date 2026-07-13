import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode
import yaml
import re

# from utils import create_leaderboard

def normalize_column_name(df):
    result = []
    for col in df.columns:
        col = re.sub('(\n|\t)', '', col) # replace \n and \t with ''
        col = col.lower() # lower
        col = re.sub(' ', '_', col) # repace ' ' with '_'
        col = unidecode(col) # remove accent

        result.append(col)

    df.columns = result

    return df

def create_leaderboard(scenario):
    """
    Create the leaderboard based on scenario
    """

    
    df_fact_selection = normalize_column_name(pd.read_csv(r'data\fact_selection.csv'))
    df_fact_current_round = normalize_column_name(pd.read_csv(r'data\fact_current_round.csv'))

    df_dim_team = normalize_column_name(pd.read_csv(r'data\dim_team.csv'))
    df_dim_score = normalize_column_name(pd.read_csv(r'data\dim_score.csv'))
    

    # change the df_fact_current_round based on the scenario:
    content = scenario['content']
    for team, current_round in content.items():
        df_fact_current_round.loc[df_fact_current_round['team'] == team, 'current_round'] = current_round

        if current_round == 'final':
            df_fact_current_round.loc[df_fact_current_round['team'] == team, 'team_status'] = 0
        elif current_round == 'winner':
            df_fact_current_round.loc[df_fact_current_round['team'] == team, 'team_status'] = 1

    # continue

    df_fact_current_score = df_dim_team.merge(
        df_fact_current_round
        ,left_on="team"
        ,right_on="team"
    ).merge(
        df_dim_score
        ,left_on=['pot', 'current_round']
        ,right_on=['pot', 'round']
    )

    df_fact_selection['new_team_id'] = (
        df_fact_selection.merge(
            df_fact_current_score
            ,left_on='team'
            ,right_on='team'
        )
        .sort_values(by=['ticket', 'pot', 'team'])
        .groupby(['ticket']).cumcount() + 1
    )

    df_fact_selection['team_id'] = 'team_' + df_fact_selection['new_team_id'].astype(str)
    df_fact_selection = (
        df_fact_selection.drop(['new_team_id'], axis=1)
    )

    df_fact_score = df_fact_selection.merge(
            df_fact_current_score
            ,left_on='team'
            ,right_on='team'
        ).assign(team = lambda x: x['team'] + ' (pot ' + x['pot'].astype(str) + ')')

    df_fact_score_agg =(
        df_fact_selection.merge(
            df_fact_current_score
            ,left_on='team'
            ,right_on='team'
        )
        .sort_values(by=['pot'])
        .groupby(['ticket'])
        .agg(
            total_score = ('score', 'sum')
            ,pot_selected = ('pot', lambda x: ''.join(x.astype(str)))
            ,pot_avg = ('pot', 'mean')
        )
        .reset_index()
        .sort_values(by='total_score', ascending=False)
        .reset_index(drop=True)
    )

    df_fact_score_agg['rank'] = df_fact_score_agg.index + 1

    def create_df_team():
        # Create an empty dictionary to hold all our DataFrames
        team_dfs = {}
        
        for i in [1, 2, 3, 4]:
            # Assign each new DataFrame to a dynamically named dictionary key
            team_dfs[f'df_team_{i}'] = (
                df_fact_score[df_fact_score['team_id'] == f'team_{i}']
                .rename(columns={
                    'team': f'team_{i}',
                    'current_round': f'round_{i}',
                    'score': f'score_{i}'
                })
                [['ticket', f'team_{i}', f'round_{i}', f'score_{i}']]
            )
            
        return team_dfs


    list_cols = ['rank','ticket', 'total_score', 'pot_selected']
    for i in [1,2,3,4]:
        list_cols += [f"team_{i}", f"round_{i}", f"score_{i}"]

    df_fact_score_agg = (
        df_fact_score_agg
        .merge(
            create_df_team()['df_team_1']
            ,left_on='ticket'
            ,right_on='ticket'
        )
        .merge(
                create_df_team()['df_team_2']
                ,left_on='ticket'
                ,right_on='ticket'
        )
        .merge(
            create_df_team()['df_team_3']
            ,left_on='ticket'
            ,right_on='ticket'
        )
        .merge(
            create_df_team()['df_team_4']
            ,left_on='ticket'
            ,right_on='ticket'
        )
    )[list_cols]

    return df_fact_score_agg


def render_scenario():
    scenario_path = r"data/scenario.yaml"
    with open(scenario_path, "r", encoding='utf-8') as file:
        scenario_file = yaml.safe_load(file)

    list_scenario_name = []

    for i, scenario in enumerate(scenario_file['scenario']):
        list_scenario_name.append(scenario['name'])


    if 'active_scenario' not in st.session_state:
        st.session_state.active_scenario = 1

    # 2. Create a clean layout (2 rows of 4 buttons)
    st.subheader("Chọn kịch bản")
    row1 = st.columns(4)
    row2 = st.columns(4)

    # 3. Generate the 8 buttons
    for i in range(1, 9):
        # Decide which row the button belongs to
        col = row1[i-1] if i <= 4 else row2[i-5]

        


        # Create the button and update memory if clicked
        if col.button(f"{list_scenario_name[i-1]}", use_container_width=True):
            st.session_state.active_scenario = i
            



    st.divider()

    


    dict_round_decode = {
        'group_stage': 1
        ,'32_team': 2
        ,'16_team': 3
        ,'quarter_final': 4
        ,'semi_final': 5
        ,'final': 6
        ,'winner': 7
    }

    

    df = create_leaderboard(scenario_file['scenario'][st.session_state.active_scenario - 1])
    list_cols_round = [col for col in df.columns if 'round' in col and 'decode' not in col]
    list_cols_round_decode = []
    for col in list_cols_round:
        list_cols_round_decode.append(f'{col}_decoded')
        df[f'{col}_decoded'] = df[col].map(dict_round_decode)


    df['round_agg'] = (
        df[list_cols_round_decode]
        .astype(str).agg(''.join, axis=1)
        .apply(lambda row: int(''.join(sorted(list(row), reverse=True))))
    )


    df = (
        df
        .drop(list_cols_round_decode, axis=1)
        .sort_values(by=['total_score', 'round_agg'], ascending=[False, False])
    )

    df['rank'] = df[['total_score', 'round_agg']].apply(lambda row: tuple(row), axis=1).rank(method='min', ascending=False).astype(int)
    df = df.drop(['round_agg'], axis=1)


    display_df = df.rename({
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

    ##################
    # highlight teams
    ##################
    df_fact_current_round = pd.read_csv("data/fact_current_round.csv")
    status_dict = dict(zip(df_fact_current_round['team'], df_fact_current_round['team_status']))

    display_df = display_df \
            .style.set_properties(
                subset=score_cols, 
                **{'font-weight': 'bold'}
            ) 

    st.markdown(scenario_file['scenario'][st.session_state.active_scenario-1]['name'])
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=dynamic_height)
        

    