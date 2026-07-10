import streamlit as st

# 1. Metadata for the Discussion List
ID = 11
TITLE = "Nhận định tứ kết wc 26: Liệu có bất ngờ (phần 1)"
AUTHOR = "Nguyễn Duy Đăng"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():

    st.markdown('WC đã đi dần tới những trận đấu cuối cùng, 8 cái tên còn lại đều xứng đáng với những gì họ đã thể hiện ở các vòng đấu trước. Cùng mình điểm qua 4 trận tứ kết được dự báo sẽ rất hấp dẫn và đầy những bất ngờ đang chờ đón chúng ta.')

    st.subheader('Trận 1: Pháp vs Ma Rốc')

    st.markdown('Nhà đường kim á quân đang có một phong độ hủy diệt sau những chiến thắng trước Đức và Paraguay. “Độc tài” Mbappe có 7 bàn thắng, Olise chói sáng với 6 kiến tạo, cùng tất cả các đồng đội còn lại tạo nên một tuyển Pháp hùng mạnh, ứng cử viên hàng đầu cho chức vô địch.')

    st.markdown('Ở bên kia, nhà đường kim vô địch CAN, Ma Rốc cũng thể hiện một bộ mặt tích cực khi lần lượt đánh bại Hà Lan và chủ nhà Canada để tiến vào vòng tứ kết. Lối chơi trực diện, dựa vào thể lực nhưng cũng rất kỹ thuật của các học trò hlv Mohamed Ouahbi sẽ là thước đo lớn đầu tiên cho Mbappe và các đồng đội.')

    st.markdown('**Dự đoán: Pháp 2-1 Ma Rốc**')

    st.subheader('Trận 2: Tây Ban Nha vs Bỉ')

    st.markdown('Chưa thủng lưới 1 bàn nào từ đầu giải đấu, hãy nhớ tới điều này. Tây Ban Nha (TBN) đang là đội có hàng tiền vệ kiểm soát tốt nhất ở WC năm nay với một Rodri phiên bản 2024 và Pedri “không phải đá AM” và Olmo di chuyển tự do. Những cũng đừng quên hàng công của Bò tót, Oyarzabal đang có phong độ cao và một Yamal dần trở lại với những bước chạy thanh thoát. Tất cả tạo nên 1 ứng cử viên vô địch, một đối trọng thật sự đủ cân lạng với Pháp hay Argentina. Chiến thắng trước Bồ Đào Nha của CR7 đã khẳng định điều đó một cách rõ ràng.')

    st.markdown('Bỉ có một khởi đầu không như ý, nhưng dường như sau lứa thế hệ vàng De Bruyne, Hazard, … Bỉ đã thực sự cân bằng hơn và càng đi sâu đá càng hay. Đầu tàu Leandro Trossard sẽ là một thách thức lớn cho hàng thủ TBN. Tuy nhiên hàng thủ lại là nỗi lo của Bỉ, Courtois liệu có thể “một mình cân hết” ?. Tất cả chờ đón chúng ta trong trận đấu này.')

    st.markdown('**Dự đoán TBN 3-1 Bỉ**')