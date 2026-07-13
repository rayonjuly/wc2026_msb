import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from unidecode import unidecode
import yaml

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

    
    df_fact_selection = normalize_column_name(pd.read_csv(r'..\\data\fact_selection.csv'))
    df_fact_current_round = normalize_column_name(pd.read_csv(r'..\data\fact_current_round.csv'))

    df_dim_team = normalize_column_name(pd.read_csv(r'..\\data\dim_team.csv'))
    df_dim_score = normalize_column_name(pd.read_csv(r'..\\data\dim_score.csv'))
    

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