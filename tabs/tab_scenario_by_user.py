import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode
import re

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

def render_scenario_by_user():
    df = pd.read_csv(r"data/scenario_by_user.csv")
    df = df.fillna('')
    df['Kịch bản top 1'] = df['Kịch bản top 1'].astype(str).str.replace(';', '\n')
    df['Kịch bản top 3'] = df['Kịch bản top 3'].astype(str).str.replace(';', '\n')

    df = df.replace(0, '') 
    dim_user = df['User'].tolist()

    dropdown_user = ['Tất cả'] + dim_user
    selected_user = st.selectbox('Lọc theo người chơi:', dropdown_user, key="user_filter_selectbox")

    mask_user = pd.Series(True, index=df.index)

    if selected_user != "Tất cả":
        mask_user = df['User'].str.contains(selected_user)

    mask = mask_user 
    display_df = df[mask]
    display_df = display_df.style.set_properties(**{'white-space': 'pre-wrap'})
    # Force a line break (\n) before every new scenario starts
    
    html_table = display_df.to_html(escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    
    # st.dataframe(
    #     display_df,
    #     column_config={
    #         "Kịch bản top 1": st.column_config.TextColumn("Kịch bản top 1", width="large"),
    #         "Kịch bản top 3": st.column_config.TextColumn("Kịch bản top 3", width="large")
    #     },
    #     use_container_width=True
    # )

    # st.table respects \n perfectly and will create distinct visual lines
    # st.table(display_df)