import streamlit as st

# 1. Metadata for the Discussion List
ID = 4
TITLE = "Bóng đá không liên quan đến chính trị - trò hề của FIFA"
AUTHOR = "Trần Xuân Huy"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown('"Bóng đá không liên quan đến chính trị." Đó là câu thần chú mà FIFA và các quan chức của họ đã lặp đi lặp lại không biết bao nhiêu lần, mỗi khi có ai đó dám hỏi vì sao một tổ chức thể thao lại liên tục vướng vào những quyết định mang màu sắc chính trị rõ rệt đến vậy. Chỉ tiếc rằng, càng nhìn vào World Cup 2026, câu thần chú ấy nghe càng giống một trò đùa mà FIFA tự kể cho chính mình nghe.')

    add_image(
        file_name="data/articles/6/6_1.jpg"
        ,caption="Chủ tịch FIFA Gianni Infantino và tổng thống Donald Trump phát biểu tại một sự kiện của World Cup 2026"
    )
    st.markdown('**Khi "trung lập" chỉ là một chiều**')

    st.markdown('Ngay từ vòng loại, Nga đã bị loại khỏi World Cup 2026 vì cuộc chiến tại Ukraine — một quyết định gắn liền hoàn toàn với địa chính trị, không phải bóng đá. FIFA khi đó không hề né tránh việc đưa chính trị vào sân cỏ: đây là phản ứng trước một cuộc xung đột quốc tế, và tổ chức này sẵn sàng dùng quyền lực của mình để đứng về một phía. Không ai trách cứ nguyên tắc đó cả — vấn đề là, nếu bóng đá thực sự "không liên quan đến chính trị", thì quyết định ấy đến từ đâu?')

    st.markdown('Câu trả lời trở nên rõ ràng hơn khi nhìn sang đội tuyển Iran tại chính kỳ World Cup này. Được tổ chức một phần trên đất Mỹ, đội bóng Iran đã phải vật lộn với hàng loạt rào cản: nhiều thành viên ban huấn luyện và quản lý bị từ chối visa, đội phải đóng trại tại Tijuana (Mexico) thay vì trên đất Mỹ, chỉ được phép nhập cảnh trong vòng chưa đầy 24-48 giờ trước mỗi trận và phải rời đi ngay sau khi tiếng còi mãn cuộc vang lên — không có cả một đêm để hồi phục. HLV đội tuyển Iran từng mô tả đội bóng của mình là "đội bị đối xử bất công nhất" tại giải đấu. Liên đoàn bóng đá Iran còn tố cáo lượng vé phân bổ cho cổ động viên nước này bị cắt giảm. Còn FIFA — tổ chức luôn khẳng định thể thao đứng ngoài chính trị — thì im lặng, hoặc nhiều lắm là đưa ra vài lời giải thích mang tính thủ tục. Vậy hóa ra, chính trị chỉ "không liên quan" đến bóng đá khi nó không được nhắc tới trực tiếp. Còn khi cần, FIFA hoàn toàn có thể để visa, chiến tranh, hay áp lực ngoại giao quyết định ai được đá, đá ở đâu, và đá trong điều kiện nào.')

    add_image(
        file_name="data/articles/6/6_2.jpg"
        ,caption="Đội tuyển Iran di chuyển từ trại huấn luyện tại Tijuana, Mexico, sang thi đấu trên đất Mỹ"
    )

    st.markdown('**Cú điện thoại thay đổi luật chơi**')

    st.markdown('Nhưng nếu Nga và Iran cho thấy chính trị có thể cản trở một đội tuyển, thì câu chuyện của Folarin Balogun lại cho thấy chính trị cũng có thể cứu một cầu thủ — miễn là cú điện thoại đến từ đúng người.')

    st.markdown('Sau khi nhận thẻ đỏ trong trận gặp Bosnia và Herzegovina, Balogun đối mặt án treo giò tự động một trận theo đúng quy định của FIFA — điều mà chính tổ chức này xác nhận là không thể kháng cáo. Nhưng rồi Tổng thống Mỹ Donald Trump đã đích thân gọi điện cho Chủ tịch FIFA Gianni Infantino để "xem xét lại" tấm thẻ đỏ ấy. Vài ngày sau, FIFA viện dẫn một điều khoản kỷ luật hiếm khi được sử dụng để hoãn thi hành án phạt, cho phép Balogun ra sân đá chính trong trận gặp Bỉ ở vòng 16 đội — lần đầu tiên trong hơn 60 năm lịch sử World Cup một quyết định như vậy được đảo ngược theo cách này.')

    st.markdown('Liên đoàn bóng đá Bỉ kháng cáo. FIFA bác đơn, thậm chí không cung cấp đầy đủ lý do bằng văn bản mà Bỉ yêu cầu. UEFA lên tiếng gọi đây là điều "khó tin và không thể biện minh". Cựu Chủ tịch FIFA Sepp Blatter thì thẳng thắn hơn: thẻ đỏ không nên bị lật ngược bởi những cuộc điện thoại chính trị, mà chỉ nên bởi luật lệ, bằng chứng và các cơ quan độc lập.')

    st.markdown('Trớ trêu thay, tất cả sự can thiệp ấy cuối cùng chẳng thay đổi được điều gì trên bảng tỷ số. Bỉ bước vào trận đấu và chơi một trong những màn trình diễn thuyết phục nhất giải, thắng đậm 4-1, khiến mọi tranh cãi về sự hiện diện của Balogun trở nên gần như vô nghĩa về mặt chuyên môn.')

    add_image(
        file_name="data/articles/6/6_3.jpg"
        ,caption="Các cầu thủ Bỉ ăn mừng chiến thắng 4-1 trước Mỹ tại vòng 16 đội, Seattle, ngày 6/7/2026"
    )

    st.markdown('Ấy vậy mà, chính vì cú điện thoại của ông Trump, một chiến thắng xứng đáng của Bỉ lại bị phủ bóng bởi nghi ngờ, còn thất bại của tuyển Mỹ — thay vì được nhìn nhận như một trận thua đơn thuần trước đối thủ mạnh hơn — lại gắn liền với hình ảnh một đội tuyển rời giải trong sự hoài nghi, chứ không phải trong sự tôn trọng mà một đối thủ chơi sòng phẳng lẽ ra xứng đáng nhận được. Nếu không có sự can thiệp ấy, có lẽ tuyển Mỹ đã có thể rời World Cup theo cách nhẹ nhàng hơn nhiều: thua một trận đấu đẹp, trước một đối thủ chơi hay hơn, và nhận được sự cảm thông thay vì những dấu hỏi về tính chính danh của trận đấu.')

    st.markdown('Một tổ chức luôn miệng nói bóng đá đứng ngoài chính trị, hóa ra lại sẵn sàng viết lại chính luật lệ của mình chỉ sau một cuộc gọi từ Nhà Trắng — để rồi cái giá phải trả không chỉ là uy tín của FIFA, mà còn là danh dự thi đấu của chính đội tuyển mà cuộc gọi ấy định bảo vệ.')

    st.markdown('Trò hề mang tên "trung lập"')

    st.markdown('Đặt cạnh nhau, ba câu chuyện ấy vẽ nên một bức tranh không thể rõ ràng hơn: FIFA không hề đứng ngoài chính trị. Họ chỉ chọn lọc khi nào nên nhắc đến nó, và khi nào nên giả vờ nó không tồn tại. Chính trị bị viện ra để loại một đội tuyển. Chính trị âm thầm định hình đội tuyển được chào đón ra sao trên sân nhà của chính giải đấu. Và chính trị, khi cần, có thể xóa sạch một tấm thẻ đỏ chỉ bằng một cuộc điện thoại.')

    st.markdown('Câu khẩu hiệu "bóng đá không liên quan đến chính trị" vì vậy không còn là một nguyên tắc, mà đã trở thành một tấm khiên tiện lợi — được giương lên mỗi khi FIFA muốn tránh né trách nhiệm, và cất đi mỗi khi chính trị mang lại lợi ích cho họ. Nếu FIFA thực sự muốn được nhìn nhận là một tổ chức trung lập, có lẽ họ nên bắt đầu bằng việc đối xử nhất quán với các đội tuyển và cầu thủ của mình — thay vì để mức độ "trung lập" phụ thuộc vào việc ai đang gọi điện ở đầu dây bên kia.')

