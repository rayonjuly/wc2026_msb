import streamlit as st

# 1. Metadata for the Discussion List
ID = 10
TITLE = "Vòng tứ kết WC 2026: Những gã khổng lồ đối diện với những kẻ thách thức"
AUTHOR = "Trần Xuân Huy"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown('Vòng tứ kết World Cup 2026 đã chính thức lộ diện với bốn cặp đấu đầy kịch tính, diễn ra tại Mỹ trong các ngày 9-11/7. Điều thú vị là bốn "gã khổng lồ" của bóng đá thế giới - Pháp, Tây Ban Nha, Argentina, Anh - đều phải đối đầu với những "kẻ thách thức" giàu tham vọng: Morocco, Bỉ, Thụy Sĩ và đặc biệt là hiện tượng Na Uy. Pháp, Morocco, Na Uy, Anh, Tây Ban Nha, Bỉ, Argentina và Thụy Sĩ đều đã giành được suất vào vòng tứ kết, với bốn trận đấu bom tấn sẽ diễn ra khắp nước Mỹ')

    add_image(
            file_name="data/articles/10/10_1.jpg"
            ,caption=""
        )

    st.markdown("**Pháp vs Morocco - Cuộc Tái Đấu Lịch Sử**")

    st.markdown('Cặp đấu mở màn vòng tứ kết là màn tái hiện trận bán kết World Cup 2022 tại Qatar, khi Pháp từng dập tắt câu chuyện cổ tích của Morocco. Lần này, Morocco bước vào trận đấu với phong độ cực kỳ ấn tượng: đứng đầu bảng đấu có Croatia và Bỉ, loại Tây Ban Nha trên chấm luân lưu ở vòng 1/8, rồi vượt qua Canada một cách thuyết phục để vào tứ kết. Trong khi đó, đội tuyển Pháp - hiện đang xếp hạng số 1 thế giới - đã trải qua thử thách khó khăn nhất của họ khi đánh bại một Paraguay đầy quyết tâm. Đây hứa hẹn là màn phục thù đầy cảm xúc cho "Sư tử Atlas".')

    st.markdown('**Dự đoán: Pháp thắng 1-1 (Pháp thắng Penalty)**')

    st.markdown('Pháp sở hữu chiều sâu đội hình và sức mạnh tấn công vượt trội với Mbappé đang có phong độ cao, nhưng Morocco với lối chơi phòng ngự kỷ luật và tinh thần phục thù sẽ khiến "Les Bleus" phải rất vất vả mới có thể giành vé đi tiếp, có thể phải chờ đến những loạt Penalty')

    add_image(
            file_name="data/articles/10/10_2.jpg"
            ,caption="Lợi thế cho Pháp hay bất ngờ cho anh cả châu Phi"
        )

    st.markdown("**Tây Ban Nha vs Bỉ - Hàng Thủ Thép Đối Đầu Hỏa Lực Tấn Công**")

    st.markdown('Đây được xem là cặp đấu mang tính đối lập rõ nét nhất trong bốn trận tứ kết: hàng phòng ngự tốt nhất giải đấu chạm trán một trong những hàng công nguy hiểm nhất. Tây Ban Nha, đội xếp hạng ba thế giới, chưa để thủng lưới bàn nào tại giải đấu này, với chuỗi sáu trận sạch lưới liên tiếp tại World Cup - kỷ lục dài nhất lịch sử. Ngược lại, Bỉ vừa có chiến thắng hủy diệt 4-1 trước chủ nhà Mỹ ở vòng 1/8, cho thấy sức mạnh tấn công đáng gờm với sự hiện diện của Romelu Lukaku, Kevin De Bruyne và Jérémy Doku. Tuy vậy, lịch sử đối đầu lại nghiêng hẳn về phía "La Roja": qua bảy lần chạm trán, Tây Ban Nha thắng sáu, hòa một và Bỉ chưa từng thắng nổi một trận. ')

    st.markdown('**Dự đoán: Tây Ban Nha thắng 2-0**')

    st.markdown('Với hàng thủ chưa từng bị chọc thủng lưới sau 5 trận và lối chơi kiểm soát bóng đẳng cấp, Tây Ban Nha nhiều khả năng sẽ tiếp tục giữ sạch lưới trước Bỉ. Hàng công của "Quỷ đỏ" tuy nguy hiểm nhưng lịch sử đối đầu bất lợi (0 thắng/7 trận) là một gánh nặng tâm lý không nhỏ.')

    add_image(
            file_name="data/articles/10/10_3.jpg"
            ,caption=""
        )

    st.markdown("**Argentina vs Thụy Sĩ - Cuộc Lội Ngược Dòng Ngoạn Mục Đối Đầu Bản Lĩnh Phòng Ngự**")

    st.markdown('Argentina đã có màn trình diễn đầy cảm xúc để giành vé vào tứ kết, khi bị dẫn trước Ai Cập 2-0 cho đến phút 79 nhưng cuối cùng lội ngược dòng thắng 3-2 nhờ công của Lionel Messi và các đồng đội, khép lại bằng bàn thắng ấn định của Enzo Fernández ở phút bù giờ. Ở phía đối diện, Thụy Sĩ đã thể hiện bản lĩnh thép khi cầm hòa Colombia 0-0 sau 120 phút thi đấu, rồi giành chiến thắng trên chấm luân lưu để góp mặt ở vòng tứ kết. Argentina hiện đứng thứ 3 trên bảng xếp hạng FIFA, trong khi Thụy Sĩ xếp thứ 15 - một khoảng cách không nhỏ, nhưng đội bóng châu Âu này đã chứng minh khả năng thi đấu kiên cường trong những thời khắc quyết định.')

    st.markdown('**Dự đoán: Argentina thắng 2-1 (sau 90 phút) hoặc phân định bởi hiệp phụ**')

    st.markdown('Argentina với sự tỏa sáng của Messi có sức mạnh vượt trội, nhưng hàng thủ chặt chẽ của Thụy Sĩ - đội vừa cầm hòa Colombia 0-0 - có thể khiến trận đấu trở nên giằng co và khó bứt phá. Đây là cặp đấu tiềm ẩn nguy cơ đi vào hiệp phụ hoặc luân lưu.')

    st.markdown("**Anh vs Na Uy - Cuộc Đối Đầu Của Hai Chân Sút Vĩ Đại**")

    st.markdown('Đây có lẽ là cặp đấu được mong chờ nhất vòng tứ kết, khi lần đầu tiên trong lịch sử, Na Uy góp mặt tại vòng tứ kết World Cup. Erling Haaland đã trở thành người hùng của đội tuyển "Những chú chim yến biển" khi ghi bàn thắng quyết định ở vòng 1/8 và có cú đúp giúp Na Uy tạo địa chấn hạ gục Brazil 2-1. Với 7 bàn thắng sau 5 trận, Haaland đang cùng Messi và Mbappé dẫn đầu cuộc đua Chiếc giày vàng. Ở phía bên kia, đội tuyển Anh của HLV Thomas Tuchel cũng đã có màn ngược dòng đầy kịch tính trước Mexico với tỷ số 3-2, nhờ cú đúp của Jude Bellingham và một quả phạt đền của đội trưởng Harry Kane. Cuộc so tài giữa hai chân sút hàng đầu châu Âu - Kane và Haaland - hứa hẹn sẽ định đoạt số phận trận đấu và cả cuộc đua giày vàng của giải.')

    add_image(
            file_name="data/articles/10/10_3.jpg"
            ,caption=""
        )

    st.markdown('**Dự đoán: Anh thắng 3-2 sau 90 phút hoặc giải quyết sau 120 phút**')

    st.markdown('Đây có thể là trận đấu giàu bàn thắng nhất vòng tứ kết. Cả hai đội đều để thủng lưới đều đặn trong giải, và với sự hiện diện của hai chân sút hàng đầu Kane - Haaland, khả năng cả hai đội đều ghi bàn là rất cao. Anh được đánh giá nhỉnh hơn nhờ chiều sâu đội hình và hàng thủ ổn định hơn, nhưng Haaland hoàn toàn có thể một mình định đoạt trận đấu.')

    st.markdown('**Nhận Định Chung**')

    st.markdown('Vòng tứ kết năm nay mang đến một sự tương phản thú vị: các đội bóng lớn vẫn giữ được vị thế ứng viên vô địch, nhưng những "kẻ thách thức" đã chứng minh họ không chỉ đến để tham dự. Morocco tái hiện giấc mơ 2022, Na Uy lần đầu góp mặt ở đẳng cấp này cùng hiện tượng Haaland, Bỉ mang theo thế hệ vàng cuối cùng, còn Thụy Sĩ âm thầm nhưng chắc chắn tiến bước. Bốn trận đấu, bốn câu chuyện khác nhau, nhưng tất cả đều hứa hẹn những màn kịch tính không thể rời mắt trên hành trình tìm ra bốn đội bóng cuối cùng góp mặt ở bán kết World Cup 2026.')