import streamlit as st

# 1. Metadata for the Discussion List
ID = 4
TITLE = "Đố vui 02"
AUTHOR = "Tào Lê Minh"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown("Ghép các ký tự sau thành một mệnh đề chuẩn:")

    st.markdown("7001=")