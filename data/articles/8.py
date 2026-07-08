import streamlit as st

# 1. Metadata for the Discussion List
ID = 8
TITLE = "30 năm yêu một màu áo trắng…"
AUTHOR = "Đặng Huy Hoàng"


def add_image(file_name, caption):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(file_name, caption, use_container_width=True)

# 2. The Content Renderer
def render():
    st.markdown("Có những tình yêu không bắt đầu từ một danh hiệu, mà bắt đầu từ một ký ức.")


    st.markdown("Tôi sinh ra ở một vùng quê nghèo Nam Định. Tuổi thơ gắn với những chiếc tivi đen trắng, nơi mỗi kỳ Euro hay World Cup là cả xóm ngồi chen nhau theo dõi đến khuya. Euro 1996 là cột mốc đầu tiên tôi thực sự biết thế nào là sống cùng bóng đá. Và cũng từ mùa hè ấy, tôi chọn Đội tuyển Đức.")

    st.markdown("Năm nay tôi đã 46 tuổi. Gần 30 năm đồng hành với 'Cỗ xe tăng' là gần 30 năm đi qua đủ mọi cung bậc cảm xúc. Đã từng vỡ òa vì những chiến thắng, tự hào khi họ nâng cao những chiếc cúp danh giá. Cũng đã từng lặng người trước những thất bại, tiếc nuối sau những kỳ Euro và World Cup khép lại trong nước mắt, có những đêm mất ngủ chỉ vì một trận cầu.")

    add_image(
        file_name="data/articles/8/8_1.jpg"
        ,caption="Mỗi chiếc áo là một kỉ niệm, là một nốt thăng trầm trong hành trình 30 năm vừa qua. Các bạn có thể liệt kê những mẫu áo này gắn với giải đấu lớn nào không?"
    )

    st.markdown("Đức không phải lúc nào cũng mạnh nhất. Họ cũng có những giai đoạn khủng hoảng, những lần bị loại sớm khiến người hâm mộ đau lòng. Nhưng có lẽ, chính những năm tháng ấy mới khiến tình yêu trở nên bền chặt hơn. Bởi yêu một đội bóng không phải chỉ để tận hưởng vinh quang, mà còn để cùng họ đứng dậy sau mỗi lần vấp ngã.")

    st.markdown("Giờ đây, khi mái tóc đã điểm thêm vài sợi bạc, tôi vẫn giữ nguyên thói quen năm nào: đến mỗi kỳ Euro hay World Cup, lại háo hức chờ Đội tuyển Đức ra sân như cậu bé ngồi trước chiếc tivi đen trắng ở quê năm ấy.")

    st.markdown("Có lẽ, thanh xuân rồi cũng sẽ qua. Nhưng tình yêu dành cho màu áo trắng của Đội tuyển Đức sẽ còn ở lại.")

    st.markdown("30 năm trước, tôi chọn nước Đức. Và đến hôm nay, tôi chưa từng hối hận.")

    st.markdown("Einmal Deutschland, immer Deutschland! (Một lần là người hâm mộ Đức, mãi mãi là người hâm mộ Đức.)")

    st.markdown("Immer Deutschland!")
