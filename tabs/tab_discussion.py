import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode
import datetime
import json
import os
import importlib.util # THE NEW IMPORT

# 1. Mock Data for Articles

# Define the local file path for saving comments
COMMENTS_FILE = "data/comments.json"
ARTICLES_DIR = "data/articles"

def load_articles():
    """Reads all Python files in the articles directory and extracts their metadata and render functions."""
    articles_list = []
    
    if os.path.exists(ARTICLES_DIR):
        for filename in os.listdir(ARTICLES_DIR):
            # Only process .py files (and ignore hidden __init__.py files)
            if filename.endswith(".py") and not filename.startswith("__"):
                filepath = os.path.join(ARTICLES_DIR, filename)
                module_name = filename[:-3] # Remove '.py' for the module name
                
                try:
                    # Dynamically load the Python file
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Extract the metadata and the render function
                    article_data = {
                        "id": getattr(module, "ID", 0),
                        "title": getattr(module, "TITLE", "Không có tiêu đề"),
                        "author": getattr(module, "AUTHOR", "Ẩn danh"),
                        "render_func": getattr(module, "render", None) # Grabs the function itself!
                    }
                    
                    # Only add it if the render function exists
                    if article_data["render_func"] is not None:
                        articles_list.append(article_data)
                        
                except Exception as e:
                    st.error(f"Lỗi khi load bài viết {filename}: {e}")
    else:
        os.makedirs(ARTICLES_DIR, exist_ok=True)
        
    # Sort by ID
    return sorted(articles_list, key=lambda x: x.get('id', 0))

articles = load_articles()

def load_comments():
    """Loads comments from the local JSON file. If it doesn't exist, returns empty lists."""
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # JSON keys are always strings, so we convert them back to integers to match article IDs
            return {int(k): v for k, v in data.items()}
    
    # Default fallback if the file doesn't exist yet
    return {article['id']: [] for article in articles}

def save_comments(comments_dict):
    """Saves the current dictionary of comments into the JSON file."""
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(COMMENTS_FILE), exist_ok=True)
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(comments_dict, f, ensure_ascii=False, indent=4)


def render_discussion():
    # 2. Initialize Session States (Memory)
    if "viewing_article" not in st.session_state:
        st.session_state.viewing_article = None

    if "current_user" not in st.session_state:
        st.session_state.current_user = None

    # Load comments from the local file instead of resetting them
    if "comments" not in st.session_state:
        st.session_state.comments = load_comments()

    # ==========================================
    # 3. SIMPLE LOGIN SYSTEM
    # ==========================================
    if st.session_state.current_user is None:
        st.info("👋 Hãy đăng nhập để tham gia bình luận!")
        col1, col2 = st.columns([3, 1])
        with col1:
            df = pd.read_csv(r"data/standing.csv").dropna(how='all')
            dim_user = df['ticket'].str.split(" - ").str[0].drop_duplicates().sort_values(key=lambda col: col.apply(unidecode)).tolist()
            username_input = st.selectbox('Lựa chọn tên đăng nhập:', dim_user)
        with col2:
            st.write("") # Alignment trick
            st.write("")
            if st.button("Đăng nhập", use_container_width=True):
                if username_input.strip():
                    st.session_state.current_user = username_input.strip()
                    st.rerun()
                else:
                    st.warning("Vui lòng nhập tên!")
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.success(f"👤 Đang đăng nhập dưới tên: **{st.session_state.current_user}**")
        with col2:
            if st.button("Đăng xuất", use_container_width=True):
                st.session_state.current_user = None
                st.rerun()
    
    st.markdown("---")

    # ==========================================
    # 4. ARTICLE LIST VIEW
    # ==========================================
    if st.session_state.viewing_article is None:
        for article in articles:
            # Show number of comments for each article (Ensuring we use string keys safely if needed, but integers work here)
            comment_count = len(st.session_state.comments.get(article['id'], []))
            button_label = f"🔗 {article['title']} (bởi {article['author']}) - 💬 {comment_count} bình luận"
            
            if st.button(button_label, key=f"btn_{article['id']}", use_container_width=True):
                st.session_state.viewing_article = article
                st.rerun()

    # ==========================================
    # 5. ARTICLE DETAIL & COMMENTS VIEW
    # ==========================================
    else:
        current_article = st.session_state.viewing_article
        
        # Back Button
        if st.button("⬅️ Quay lại", type="primary"):
            st.session_state.viewing_article = None
            st.rerun()
            
        # Article Header
        st.header(current_article['title'])
        st.caption(f"Tác giả: **{current_article['author']}**")
        st.write("")
        
        # --- EXECUTE THE PYTHON ARTICLE ---
        # This calls the render() function from inside the specific article_X.py file!
        current_article['render_func']()
        
        st.markdown("---")
        
        # Comments Section
        current_comments = st.session_state.comments.get(current_article['id'], [])
        st.subheader(f"Bình luận ({len(current_comments)})")
        
        # Display existing comments
        for c in reversed(current_comments):
            with st.container():
                st.markdown(f"**{c['user']}** 🕒 {c['time']}")
                st.write(c['text'])
                st.markdown("---")
        
        # Comment Input Form
        if st.session_state.current_user:
            with st.form(key=f"comment_form_{current_article['id']}"):
                new_comment = st.text_area("Viết bình luận của bạn:")
                submit_comment = st.form_submit_button("Gửi bình luận")
                
                if submit_comment:
                    if new_comment.strip():
                        # Append the new comment
                        if current_article['id'] not in st.session_state.comments:
                            st.session_state.comments[current_article['id']] = []
                            
                        st.session_state.comments[current_article['id']].append({
                            "user": st.session_state.current_user,
                            "text": new_comment.strip(),
                            "time": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                        })
                        
                        # THE FIX: Save the updated dictionary to the local JSON file
                        save_comments(st.session_state.comments)
                        
                        st.rerun()
                    else:
                        st.warning("Bình luận không được để trống!")
        else:
            st.info("🔒 Bạn cần đăng nhập ở khung phía trên để có thể bình luận.")