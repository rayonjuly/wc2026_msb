import streamlit as st

# 1. Metadata for the Discussion List
ID = 5
TITLE = "Điệu nhảy cuối buồn của CR7"
AUTHOR = "Nguyễn Duy Đăng"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown("Có những thất bại chỉ kéo dài 90 phút. Nhưng cũng có những thất bại khiến cả một thế hệ người hâm mộ chợt nhận ra thời gian là thứ không ai có thể đánh bại, kể cả Cristiano Ronaldo.")

    st.markdown("Rạng sáng nay, Bồ Đào Nha gục ngã trước Tây Ban Nha. Trên sân, Ronaldo vẫn chiến đấu như cách anh đã làm suốt hơn hai thập kỷ: chạy, pressing, tranh chấp và khát khao ghi bàn đến tận những phút cuối. Thế nhưng bóng đá ở đẳng cấp cao nhất luôn tàn nhẫn. Đôi chân của tuổi 41 không còn đủ để xoay chuyển trận đấu như những ngày anh một mình kéo cả đội bóng tiến lên.")


    add_image(
            file_name="data/articles/5/5_1.png"
            ,caption="Sự thất vọng của CR7"
        )

    st.markdown("Tiếng còi mãn cuộc vang lên. Không còn cú xoay người ăn mừng quen thuộc, không còn tiếng hô 'Siuuu' vang dội khắp khán đài. Chỉ còn Ronaldo đứng lặng, ánh mắt hướng về khoảng không vô định trước khi chậm rãi bước vào đường hầm. Đó có lẽ là điệu nhảy cuối cùng của một vũ công từng làm say đắm cả thế giới bóng đá – một điệu nhảy không có âm nhạc, chỉ có sự im lặng và nỗi tiếc nuối. Người ta từng quen với hình ảnh Ronaldo nâng cao những chiếc cúp, phá hết kỷ lục này đến kỷ lục khác. Anh khiến khái niệm 'không thể' gần như biến mất trong từ điển của mình. Nhưng ngay cả những người vĩ đại nhất cũng không thể chiến thắng quy luật của thời gian. Mỗi pha nước rút hôm nay đều chậm hơn một nhịp. Mỗi cú bật nhảy đều thấp hơn đôi chút. Và mỗi cơ hội trôi qua đều nhắc nhở rằng chương cuối của sự nghiệp đã ở rất gần.")

    st.markdown("Có thể đây chưa phải trận đấu cuối cùng của Ronaldo trong màu áo đội tuyển. Có thể anh vẫn sẽ xuất hiện ở một giải đấu nào đó, vẫn đeo tấm băng đội trưởng và vẫn chiến đấu bằng tất cả lòng kiêu hãnh. Nhưng sau thất bại trước Tây Ban Nha, người hâm mộ hiểu rằng những khoảnh khắc ấy sẽ không còn nhiều nữa.")

    st.markdown("Bóng đá rồi sẽ tiếp tục sản sinh những ngôi sao mới. Những cái tên trẻ sẽ thay nhau chinh phục các danh hiệu và lập nên những kỷ lục mới. Nhưng sẽ rất lâu nữa thế giới mới lại chứng kiến một cầu thủ có thể duy trì đỉnh cao hơn hai mươi năm, biến mọi sự hoài nghi thành động lực và khiến hàng triệu người thức trắng đêm chỉ để dõi theo từng bước chạy của mình.")

    st.markdown("Rạng sáng nay, Ronaldo không rời sân với tư cách một người chiến thắng. Nhưng anh vẫn nhận được những tràng pháo tay từ cả đồng đội lẫn đối thủ. Đó không phải sự thương hại, mà là sự tôn trọng dành cho một tượng đài đã cống hiến gần như cả cuộc đời cho bóng đá. Có lẽ, điều buồn nhất không phải là Bồ Đào Nha thua Tây Ban Nha. Mà là khi chứng kiến Cristiano Ronaldo lặng lẽ bước đi, chúng ta chợt hiểu rằng điệu nhảy cuối cùng của một huyền thoại đang dần khép lại.")

