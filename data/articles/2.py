import streamlit as st

# 1. Metadata for the Discussion List
ID = 2
TITLE = "Argentina – Ứng cử viên sáng giá cho chức vô địch."
AUTHOR = "Nguyễn Văn Khang"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():

    st.markdown("Không khó để đưa ra cái tên này cho danh sách ứng cử viên World Cup 2026. Đơn giản vì họ là đương kim vô địch của giải đấu và đến với Bắc Mỹ với một đội hình gần giống năm 2022. Và chúng ta cùng tìm hiểu những yếu tố nào khiến họ đánh giá cao như vậy:")

    # Note: Ensure the image path is relative to your main app.py folder!
    add_image(
        file_name="data/articles/2/2_1.png"
        ,caption="Nhánh đấu vòng knockout tại WC2026"
    )

    st.markdown("Đầu tiên, Argentina đang rơi vào một nhánh đấu cực kỳ dễ dàng. Sau khi kết thúc vòng bảng ở vị trí nhất bảng J, La Albiceleste chỉ phải đối đầu với những đối thủ được đánh giá yếu hơn rất nhiều như Cape Verde, Ai Cập, Thụy Sĩ hoặc Colombia. Giới chuyên môn nhận định đây là lợi thế lớn của Messi và các đồng đội so với các đội bóng khác như Pháp, Tây Ban Nha, Anh… Việc không phải gặp các đối thủ mạnh ngay từ các vòng đầu sẽ giúp Argentina giữ sức cho các trụ cột, tránh cho những chấn thương hoặc thẻ phạt không đáng có. Đồng thời, hlv Scaloni có thể để dành những quân bài chiến lược của mình.")

    st.markdown("Tiếp theo, việc đá trên đất Bắc Mỹ cũng là một lợi thế lớn của Argentina so với các đối thủ cạnh tranh vô địch khác. Múi giờ của Argentina gần với Mỹ và Mexico hơn nhiều so với các đội châu Âu, điều này giúp các cầu thủ không phải mất quá nhiều thời gian để thích nghi với việc thay đổi giờ giấc sinh hoạt. Cùng với đó là thời tiết nóng và ẩm ở Mỹ và Mexico hoàn toàn tương đồng với đất nước Nam Mỹ. Đặc biệt, cộng đồng người Argentina ở Mỹ rất đông, sẽ luôn tạo một không khí áp đảo trên khán đài trong những trận đấu của La Albiceleste.")

    st.markdown("Cuối cùng, Argentina sở hữu một đội hình được đánh giá toàn diện về mọi yếu tố. Đầu tiên, họ vẫn giữ được phần lớn bộ khung đã vô địch World Cup 2022 và tiếp tục thi đấu cùng nhau nhiều năm. Điều này giúp cho La Albiceleste thi đấu một cách cực kỳ nhuần nhuyễn và triển khai tối đa các chiến thuật do hlv đề ra. Đi sâu vào giải đấu, dễ dành nhận thấy Argentina sử dụng đội hình 4-4-2 với những cái tên quen thuộc.")
    add_image(
            file_name="data/articles/2/2_2.png"
            ,caption="Argentina đã ra sân với lineup này 3 trong 4 trận wc tính tới thời điểm hiện tại."
    )

    st.markdown("Với những Romero, Martínez và Didu, Argentina được đánh giá là đội có hàng thủ cực kỳ vững trãi với chỉ 1 bàn thua sau vòng bảng. Cùng cặp tiền vệ trung tâm Enzo và Mac Allister luôn duy trì tốt cấu trúc đội hình, khả năng kiểm soát khu trung tuyến. Một điểm nữa phải được nhắc đến chính là La Albiceleste đang sở hữu siêu sao hàng đầu thế giới là Messi. Chiến thuật của đội bóng Nam Mỹ vận hành cực kỳ đơn giản nhưng cực ký hiệu quả, đó là mọi đường bóng đều có đích đến là chiếc áo số 10. Thành tích 6 bàn thắng sau 3 trận vòng bảng của M10 là minh chứng rõ ràng nhất (nên nhớ vòng bảng cả đội Argentina ghi được 8 bàn thắng). Passmap dưới đây sẽ thể hiện rõ hơn cách vận hành của tuyển Argentina.")

    add_image(
            file_name="data/articles/2/2_3.jpg"
            ,caption="Passmap trận Argentina – Áo"
    )

    st.markdown("Kết luận, hội tụ các yếu tố “thiên thời – địa lợi – nhân hòa” kể trên, Argentina xứng đáng là cái tên số 1 cho chức vô địch World Cup 2026.")