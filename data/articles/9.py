import streamlit as st

# 1. Metadata for the Discussion List
ID = 9
TITLE = "Ai Cập – Argentina, kịch tính, tranh cãi và đẳng cấp"
AUTHOR = "Nguyễn Văn Khang"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown('Đây là một trong những trận đấu kịch tính nhất từ đầu vòng 16 đội World Cup 2026. Argentina thắng ngược Ai Cập 3-2 sau khi bị dẫn tới 2 bàn. La Albiceleste có một khởi đầu tệ hại khi bị thủng lưới sớm  sau pha đánh đầu của Yasser Ibrahim. Họ có cơ hội lớn để gỡ hòa khi được hưởng phạt đền nhưng Messi lại đá hỏng. Những phút sau đó chứng kiến các pha hãm thành liên tục đến từ Argentina với Messi dẫn dắt hàng công. Ai Cập đã có một trận đấu phòng ngự quả cảm, liên tục phong tỏa không gian trước khung thành của thủ môn Mostafa Shobeir. Điều này khiến Argentina rơi vào bế tắc, Messi bị khóa chặt trước vòng vây của các hậu vệ Ai Cập. Các cầu thủ còn lại cũng không có nhiều những pha xử lý đột biến và chỉ thuần spam tạt bóng vào trong vòng cấm – nơi các siêu tiền đạo lọt thỏm giữa các trung vệ cao to. Tấn công nhiều không ghi được bàn thắng, Argentina nhận đòn hồi mã thương sau pha phản công xuất sắc được kết thúc bởi Mostafa Ziko. Trong những giây phút tuyệt vọng nhất, Argentina đưa trung vệ Romero thường trực trong vòng cấm để đón những đường tạt bóng từ cánh phải, nơi Messi được chỉ bố trí nhắm thoát khỏi sự kèm cặp từ các hậu vệ Ai Cập. Các hậu vệ Ai Cập sau gần 80 phút hoạt động không ngừng nghỉ đã thấm mệt và không còn tỉnh táo để theo kèm các mũi nhọn bên phía Argentina. La Albiceleste liên tục ghi 3 bàn cuối trận để có màn lội ngược dòng kịch tính. Messi thể hiện đẳng cấp với 1 bàn 1 kiến tạo. Mặc dù thất bại, Ai Cập xứng đáng được nhận những lời khen với chiến thuật phòng ngự phản công đơn giản nhưng đầy hiệu quả. ')

    st.markdown('Kết thúc trận đấu thì đã nổ ra tranh cãi  về một loạt tình huống trong trận với nghi vấn trọng tài ưu ái đội bóng Nam Mỹ. Người viết xin phép được nhặt ra một vài tình huống đáng chú ý để các độc giả cùng thảo luận:')

    st.markdown('**VAR hủy bàn thắng nâng tỷ số lên 2-0 của Ai Cập :**')

    st.markdown('Đây là tình huống gây tranh cãi nhất trận. Đầu hiệp hai, Hassan đi bóng qua nhiều cầu thủ Argentina, xâu kim Tagliafico rồi phối hợp với Mohamed Salah trước khi Mostafa Ziko sút vào lưới, tưởng như nâng tỷ số lên 2-0. Ban đầu trọng tài công nhận bàn thắng. Tuy nhiên, VAR người Pháp Jerome Brisard đề nghị Letexier xem lại tình huống. Sau khi ra màn hình, trọng tài Pháp xác định Marwan Attia đã phạm lỗi với Lisandro Martinez ở thời điểm khởi đầu pha phản công, trước khi toàn bộ tình huống ghi bàn diễn ra. Bàn thắng bị hủy.')

    add_image(
            file_name="data/articles/9/9_1.jpg"
            ,caption="Tình huống tranh cãi đầu tiên"
        )

    st.markdown('Phía Ai Cập cho rằng Attia chỉ có va chạm rất nhẹ, là một tình huống tranh chấp bình thường và không đáng để cắt đứt cả pha bóng, cùng với đó họ viện dẫn tình huống Messi ghi bàn trong trận đấu với Áo khi Alexis MacAllister có thể đã phạm lỗi với Xaver Schlager ở giữa sân.')
    
    st.markdown('**Molina thoát thẻ đỏ sau pha va chạm không bóng**')

    st.markdown('Một tình huống khác cũng khiến Ai Cập bất bình là pha va chạm giữa Nahuel Molina và Emam Ashour ở phút thứ sáu. Trong lúc bóng không ở gần, hậu vệ Argentina dùng tay đẩy vào mặt tiền vệ Ai Cập.')
    
    add_image(
            file_name="data/articles/9/9_2.jpg"
            ,caption="Tình huống tranh cãi thứ hai"
        )

    st.markdown('Tuy nhiên, Letexier không cắt còi, còn VAR cũng không yêu cầu xem lại.')

    st.markdown('**Yêu cầu phạt đền của Ai Cập bị bỏ qua trước bàn quyết định của Argentina**')

    st.markdown('MacAllister cũng bị cho là đã kéo áo Hamdi Fathy khiến tiền vệ Ai Cập ngã trong cấm địa. Letexier không cắt còi, còn VAR cũng không yêu cầu xem lại. Đây là tình huống khá rõ ràng và phía bên Ai Cập phản ứng rất dữ dội. Rất dễ hiểu vì ngay sau đó vài phút Argentina nâng tỉ số 3-2.')

    add_image(
        file_name="data/articles/9/9_3.jpg"
        ,caption="Tình huống tranh cãi thứ ba"
        )

    st.markdown('Còn tình huống va chạm của Mo Salah thì theo quan điểm cá nhân là không thổi phạt là hợp lý.')

    st.markdown('**Kết**')

    st.markdown('Mặc dù vượt qua Ai Cập một cách đầy chật vật và tranh cái, Argentina vẫn thể hiện bản lĩnh của ứng cử viên hàng đầu cho ngôi vô địch năm nay. Với Ai Cập, họ có quyền tự hào với những gì đã thể hiện trước nhà vô địch')

    add_image(
        file_name="data/articles/9/9_4.png"
        ,caption="Chia sẻ của một fan Argentina sau bàn thua thứ 2"
        )