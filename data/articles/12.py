import streamlit as st

# 1. Metadata for the Discussion List
ID = 12
TITLE = "Dư âm sau trận Argentina - England"
AUTHOR = "Nguyễn Hữu Long"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():

    st.markdown('Trận bán kết World Cup 2026 giữa Argentina và Anh đã mang đến một màn so tài hấp dẫn. Với bản lĩnh và tinh thần thi đấu kiên cường, Argentina lội ngược dòng thắng 2-1 để giành vé vào chung kết.')

    st.markdown('Messi đúng là “gừng càng già càng cay”. Không cần quá phô trương, anh vẫn tỏa sáng bằng đẳng cấp của một huyền thoại. Trên thảm cỏ dường như có 1 thứ tôn giáo mang tên Lionel Messi, Argentina không phải có 11 cầu thủ họ có 1 chúa tể và 10 kẻ sẵn sàng tử vì đạo.')

    st.markdown('Chiến thắng của Argentina cho thấy tài năng chỉ thực sự tỏa sáng khi đi cùng ý chí và tinh thần không bỏ cuộc. Dù dừng bước, đội tuyển Anh vẫn xứng đáng nhận được sự tôn trọng vì đã cống hiến một trận đấu đầy nỗ lực và cảm xúc.')