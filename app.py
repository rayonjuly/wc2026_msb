import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode



from tabs.tab_leaderboard import render_leaderboard
from tabs.tab_rules import render_rules
from tabs.tab_bracket import render_bracket
from tabs.tab_discussion import render_discussion
from tabs.tab_scenario import render_scenario
from tabs.tab_scenario_by_user import render_scenario_by_user

import streamlit_analytics2 as streamlit_analytics

# Wrap your entire app logic inside this context manager
with streamlit_analytics.track():

    st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
    st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")
    st.caption("Cập nhật đến sau trận đấu Argentina - Switzerland")

    tab_leaderboard, tab_scenario, tab_scenario_by_user, tab_score_rules, tab_rules, tab_bracket, tab_discussion = st.tabs(["BXH hiện tại", "BXH theo kịch bản", "Kịch bản vào top theo user", "Cách tính điểm", "Luật", "Phân nhánh", "Tạp chí"])

    with tab_leaderboard:
        render_leaderboard()

    with tab_scenario:
        render_scenario()

    with tab_scenario_by_user:
        render_scenario_by_user()

    with tab_score_rules:
        st.image("Scoring_rule.png")


    with tab_rules: 
        render_rules()

    with tab_bracket:
        render_bracket()

    with tab_discussion:
        render_discussion()
