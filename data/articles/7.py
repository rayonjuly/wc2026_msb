import streamlit as st

# 1. Metadata for the Discussion List
ID = 7
TITLE = "Hành trình cuối cùng: Lời tri ân dành cho Cristiano Ronaldo tại World Cup"
AUTHOR = "Trần Xuân Huy"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown('Ngày 6/7/2026, tại sân AT&T Stadium (Arlington, Texas), World Cup của Cristiano Ronaldo đã khép lại theo cách không ai mong muốn — thất bại 0-1 trước Tây Ban Nha ở vòng 16 đội, với bàn thắng muộn của Mikel Merino. Đó cũng là dấu chấm hết cho hành trình 23 năm, sáu kỳ World Cup của một trong những cầu thủ vĩ đại nhất lịch sử bóng đá. Hãy cùng nhìn lại cả chặng đường ấy.')

    st.markdown('**Đức 2006 — Chàng trai 21 tuổi và giấc mơ bắt đầu**')

    add_image(
        file_name="data/articles/7/7_1.jpg"
        ,caption="Ronaldo tại mùa hè 2006 ở Đức"
    )

    st.markdown('Ronaldo bước vào World Cup đầu tiên năm 2006 khi mới 21 tuổi. Anh ghi bàn đầu tiên trong sự nghiệp World Cup từ chấm phạt đền trong trận gặp Iran, giúp Bồ Đào Nha thắng 2-0, và trở thành cầu thủ Bồ Đào Nha trẻ nhất từng ghi bàn tại một kỳ World Cup. Năm đó, Bồ Đào Nha tiến vào bán kết — đây vẫn là thành tích sâu nhất mà Ronaldo từng đạt được ở giải đấu này trong suốt sự nghiệp, dù sau này anh còn chơi thêm năm kỳ World Cup nữa.')
    st.markkdown("**Nam Phi 2010, Brazil 2014 — Những năm tháng ở đỉnh cao phong độ**")

    st.markdown('Ở tuổi sung sức nhất, khi đang thống trị bóng đá châu Âu cùng Real Madrid, Ronaldo vẫn không thể đưa Bồ Đào Nha tiến xa tại World Cup. Cả hai kỳ giải này, đội tuyển của anh đều dừng bước sớm, để lại cảm giác tiếc nuối rằng phong độ cấp câu lạc bộ chưa từng được tái hiện trọn vẹn trên sân khấu World Cup.')

    st.markdown('**Nga 2018 — Hat-trick huyền thoại và bản lĩnh của một nhà vô địch châu Âu**')

    add_image(
            file_name="data/articles/7/7_3.jpg"
            ,caption="Cú hattrick của Ronaldo tại Nga trước TBN"
        )

    st.markdown('Sau khi cùng Bồ Đào Nha vô địch Euro 2016 — danh hiệu lớn duy nhất trong màu áo tuyển quốc gia mà Ronaldo từng có được — anh bước vào World Cup 2018 với một trong những màn trình diễn cá nhân đáng nhớ nhất sự nghiệp: cú hat-trick trong trận hòa kịch tính 3-3 trước Tây Ban Nha ở trận mở màn, bao gồm một cú sút phạt đẳng cấp ở phút bù giờ. Đó là một trong những khoảnh khắc được nhắc đến nhiều nhất khi người ta nói về Ronaldo tại World Cup.')

    st.markdown('**Qatar 2022 — Những giọt nước mắt và chiếc ghế dự bị**')

    add_image(
        file_name="data/articles/7/7_5.jpg"
        ,caption="Giọt nước mắt của Ronaldo sau khi bị Morocco loại"
        )

    st.markdown('Ở Qatar 2022, khoảnh khắc gây xúc động mạnh nhất không phải là bàn thắng, mà là hình ảnh Ronaldo rời sân trong nước mắt sau khi Bồ Đào Nha bị Morocco loại ở tứ kết — một kết thúc đầy cay đắng cho kỳ World Cup mà nhiều người khi đó đã nghĩ là lần cuối cùng của anh.')

    st.markdown('**Bắc Mỹ 2026 — Hành trình cuối cùng, và một lời chia tay đẹp**')

    add_image(
        file_name="data/articles/7/7_6.jpg"
        ,caption="Ronaldo đã khẳng định 2026 là kì WC cuối cùng."
        )


    st.markdown('Ở tuổi 41, không ai chắc chắn Ronaldo còn đủ sức tỏa sáng ở đẳng cấp cao nhất. Trận ra quân gặp CHDC Congo, anh có một trong những màn trình diễn tệ nhất sự nghiệp World Cup: không bàn thắng, không kiến tạo, và phần lớn các đường chuyền của anh đi ngược về phía sau. Nhiều người đặt câu hỏi liệu đây có phải là dấu hiệu của một sự nghiệp đang khép lại trong lặng lẽ.')

    st.markdown('Nhưng rồi mọi thứ thay đổi. Trong trận gặp Uzbekistan, Ronaldo ghi cú đúp, trở thành cầu thủ lớn tuổi nhất từng lập một cú đúp tại World Cup, đồng thời là cầu thủ đầu tiên trong lịch sử ghi bàn ở sáu kỳ World Cup khác nhau. Ở vòng 32 đội gặp Croatia, anh ghi bàn từ chấm phạt đền — bàn thắng đầu tiên trong sự nghiệp của anh ở vòng knock-out World Cup, sau tổng cộng 23 lần ra sân tại giải đấu này.')

    st.markdown('Trước trận gặp Tây Ban Nha ở vòng 16 đội, Ronaldo đã xác nhận: đây sẽ là kỳ World Cup cuối cùng của anh. Anh nói đây là kỳ World Cup mà anh cảm nhận rõ nhất tình cảm của người hâm mộ, "về mặt cảm xúc, là kỳ World Cup đẹp nhất." Trận đấu kết thúc với tỷ số 1-0 nghiêng về Tây Ban Nha, bàn thắng đến ở phút bù giờ hiệp hai. Ronaldo rời sân trong nước mắt, nhưng khẳng định ra đi với "lương tâm thanh thản, không phải 100%, mà là 1000%."')

    st.markdown('**Những con số của một huyền thoại**')

    st.markdown('Khi khép lại sự nghiệp World Cup, Ronaldo để lại một bảng thành tích không ai sánh kịp về độ bền và sự ổn định:')

    st.markdown("""
        * 6 kỳ World Cup liên tiếp tham dự (2006–2026)
        * 27 trận đấu — nhiều thứ nhì mọi thời đại, chỉ sau Lionel Messi (30 trận)
        * 11 bàn thắng, đồng hạng 9 trong danh sách ghi bàn nhiều nhất lịch sử World Cup
        * Cầu thủ duy nhất trong lịch sử ghi bàn ở sáu kỳ World Cup khác nhau
    """)

    st.markdown('Điều duy nhất còn thiếu trong bộ sưu tập vĩ đại của anh là chiếc cúp vàng World Cup — nhưng như HLV Roberto Martínez đã nói sau trận đấu cuối cùng: "Chúng ta đang nói về một biểu tượng của bóng đá. Không có nhiều Cristiano Ronaldo trên đời. Chúng ta phải biết ơn vì những gì anh ấy đã làm ở World Cup này — với tư cách một cầu thủ, một đội trưởng, và ở cấp độ con người."')

    st.markdown('**Lời tri ân**')

    st.markdown('Từ chàng trai 21 tuổi ghi bàn đầu tiên trước Iran năm 2006, đến người đàn ông 41 tuổi rơi nước mắt rời sân ở Texas hai mươi năm sau, Cristiano Ronaldo đã dành trọn phần đẹp nhất của sự nghiệp cho tấm áo tuyển Bồ Đào Nha và cho sân khấu World Cup. Anh không có được chiếc cúp vàng mà nhiều đồng nghiệp cùng thời sở hữu, nhưng đã để lại thứ có lẽ còn giá trị hơn: sáu kỳ World Cup liên tiếp, hai mươi ba năm cống hiến không mệt mỏi, và một tình yêu với trái bóng chưa từng phai nhạt dù ở đỉnh cao hay trong những giọt nước mắt thất bại.')

    st.markdown('Ronaldo không cần chiếc cúp World Cup để chứng minh mình là ai. Danh dự của anh chưa bao giờ nằm ở những gì giành được, mà nằm ở cách anh theo đuổi nó — không bao giờ ngừng tin, không bao giờ ngừng cố gắng, cho đến tận trận đấu cuối cùng ở tuổi 41. Cảm ơn anh, vì đã cho tất cả chúng ta thấy thế nào là sống trọn vẹn với một giấc mơ, dù giấc mơ ấy có trở thành hiện thực hay không.')

