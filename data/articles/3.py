import streamlit as st

# 1. Metadata for the Discussion List
ID = 3
TITLE = "Đố vui 01"
AUTHOR = "Tào Lê Minh"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown("Trong số những cầu thủ sau, ai có nhiều bàn thắng nhất, ai có ít bàn thắng nhất trong tất cả các kì WC?")

    st.markdown("* Niklas Bendtner \n * Zlatan Ibrahimovic \n * Gareth Bale \n * Mesut Ozil \n * Karim Benzema \n * Paulo Dybala \n * Luka Modric \n * Olivier Giroud")