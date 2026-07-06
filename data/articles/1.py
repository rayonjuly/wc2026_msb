import streamlit as st

# 1. Metadata for the Discussion List
ID = 1
TITLE = "Argentina 3-2 Cape Verde: Thất bại của tỷ số, chiến thắng của lòng quả cảm"
AUTHOR = "Trần Xuân Huy"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown("Có những trận đấu mà bảng tỷ số chỉ kể được một nửa câu chuyện. Cuộc đối đầu giữa Argentina và Cape Verde ở vòng 1/32 World Cup 2026 là một trận như thế. Argentina giành chiến thắng 3-2 sau 120 phút nghẹt thở để tiếp tục hành trình bảo vệ ngôi vương. Nhưng khi tiếng còi mãn cuộc vang lên, những tràng pháo tay lớn nhất lại dành cho các cầu thủ Cape Verde – đội bóng đến từ quốc đảo chỉ hơn nửa triệu dân nhưng đã khiến cả thế giới phải ngả mũ thán phục.")
    
    # Note: Ensure the image path is relative to your main app.py folder!
    add_image(
        file_name="data/articles/1/1_1.png"
        ,caption="Bàn thắng ấn định tỷ số của Romero ở hiệp phụ thứ 2"
    )

    st.markdown("**Nhà vô địch đã đi tiếp, nhưng không hề dễ dàng**")
    st.markdown("Đúng với đẳng cấp của mình, Argentina mở tỷ số nhờ khoảnh khắc thiên tài của Lionel Messi. Tuy nhiên, Cape Verde không hề sụp đổ. Họ kiên nhẫn, tổ chức phòng ngự chặt chẽ và chờ đợi cơ hội phản công. Deroy Duarte đưa trận đấu trở lại vạch xuất phát bằng bàn gỡ đầy lạnh lùng. Bước sang hiệp phụ, Lisandro Martínez một lần nữa giúp Argentina vượt lên, nhưng chỉ ít phút sau, siêu phẩm của Sidny Cabral tiếp tục kéo Cape Verde trở lại cuộc chơi. Hai lần bị dẫn trước, hai lần gỡ hòa trước nhà đương kim vô địch – đó là minh chứng rõ nhất cho bản lĩnh của đại diện châu Phi. Chỉ đến phút 111, một tình huống không may với pha phản lưới nhà sau cú đánh đầu của Cristian Romero mới khiến Cape Verde gục ngã.")

    add_image(
            file_name="data/articles/1/1_2.png"
            ,caption="Khoảnh khắc thiên tài của Messi ở hiệp 1. Cape Verde không có một thiên tài như thế nhưng họ có một sức mạnh tập thể không thể xem thường."
    )

    st.markdown("**Cape Verde – tinh thần không bao giờ đầu hàng**")
    st.markdown("Điều khiến người hâm mộ xúc động không phải là tỷ số, mà là cách Cape Verde chiến đấu. Không ngôi sao hàng đầu thế giới. Không chiều sâu đội hình. Không được đánh giá có cơ hội trước giờ bóng lăn. Suốt 120 phút, các cầu thủ áo xanh thi đấu với nguồn năng lượng dường như vô tận. Họ tranh chấp quyết liệt, pressing không biết mệt mỏi và sẵn sàng lao mình vào mọi pha bóng. Ngay cả khi Argentina liên tục tạo sức ép, Cape Verde vẫn giữ được niềm tin rằng họ có thể viết nên câu chuyện cổ tích. Thủ thành Vozinha tiếp tục có một trận đấu xuất sắc với hàng loạt pha cứu thua quan trọng, trong khi các đồng đội của anh thi đấu bằng tất cả niềm tự hào của một quốc gia nhỏ bé nhưng giàu khát vọng.")

    st.markdown("**Khi cả thế giới đứng dậy vỗ tay**")
    st.markdown("Sau trận đấu, HLV Lionel Scaloni thừa nhận Argentina đã phải trải qua một trong những trận đấu khó khăn nhất kể từ đầu giải và dành nhiều lời khen cho Cape Verde. Chính các cầu thủ Argentina cũng hiểu rằng họ vừa vượt qua một đối thủ không hề nhỏ bé về tinh thần. Trên mạng xã hội, người hâm mộ khắp thế giới đồng loạt ca ngợi Cape Verde là đội bóng chiếm được mọi trái tim ở World Cup năm nay. Nhiều ý kiến cho rằng đây là một trong những màn trình diễn quả cảm nhất của một đội cửa dưới trong lịch sử các vòng knock-out World Cup.")


    add_image(
            file_name="data/articles/1/1_3.png"
            ,caption="Sau trận Messi cũng ca ngợi Cape Verde và thừa nhận đã có một trận đấu rất khó khăn."
    )
    st.markdown("**Lời kết**")
    st.markdown("Argentina xứng đáng đi tiếp bằng bản lĩnh của nhà đương kim vô địch. Nhưng Cape Verde mới là đội rời giải trong tư thế ngẩng cao đầu. Họ không mang về chiếc cúp, không tạo nên cú sốc lịch sử, nhưng đã mang đến điều quý giá nhất của bóng đá: niềm tin rằng lòng dũng cảm có thể thu hẹp mọi khoảng cách về đẳng cấp. Đối với một quốc gia nhỏ giữa Đại Tây Dương, hành trình tại World Cup 2026 không kết thúc bằng thất bại 2-3 trước Argentina. Nó sẽ được nhớ đến như giải đấu mà Cape Verde đã khiến cả thế giới phải đứng dậy vỗ tay – không phải vì họ chiến thắng, mà vì họ đã chiến đấu đến giây cuối cùng")
