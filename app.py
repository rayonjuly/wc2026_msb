import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode

from tabs.tab_leaderboard import render_leaderboard
from tabs.tab_rules import render_rules
from tabs.tab_bracket import render_bracket
from tabs.tab_discussion import render_discussion

st.set_page_config(page_title="Bảng xếp hạng dự đoán WC 2026 - MSB", layout="wide")
st.title("🏆 Bảng xếp hạng dự đoán WC 2026 - MSB")
st.caption("Cập nhật đến sau trận đấu England - Mexico")

tab_leaderboard, tab_score_rules, tab_rules, tab_bracket, tab_discussion = st.tabs(["Bảng xếp hạng", "Cách tính điểm", "Luật", "Phân nhánh", "Tạp chí"])

with tab_leaderboard:
    render_leaderboard()

with tab_score_rules:
    st.image("Scoring_rule.png")


with tab_rules: 
    render_rules()

with tab_bracket:
    render_bracket()

with tab_discussion:
    render_discussion()