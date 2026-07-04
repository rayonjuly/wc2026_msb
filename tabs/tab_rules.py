import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from unidecode import unidecode

def render_rules():
    st.markdown("""
        ### 📜 LUẬT CHƠI
        * **Cách thức lựa chọn:** Mỗi người chơi chọn 4 đội tuyển khác nhau trong tổng số 48 đội tham gia World Cup 2026, trong đó **1 vé = 1 lần lựa chọn 4 đội tuyển**. Người chơi có thể mua nhiều vé. Không có yêu cầu đặc biệt về việc lựa chọn giữa các vé khác nhau.
        * **Thời gian bình chọn:** Link bình chọn sẽ đóng lúc **13:00 ngày 12/06/2026**. Mọi lựa chọn ghi nhận sau thời gian này đều được coi là không hợp lệ.

        ---

        ### 🧮 CÁCH TÍNH ĐIỂM
        Tổng điểm mỗi vé là tổng điểm của cả 4 đội tuyển. Điểm của mỗi đội phụ thuộc vào việc dừng ở vòng nào và nằm ở nhóm hạt giống nào. 

        ---

        ### 🏆 THỨ TỰ ƯU TIÊN XẾP HẠNG
        Khi World Cup 2026 kết thúc, vé được xếp hạng dựa trên tổng điểm 4 đội. Trong trường hợp nhiều người chơi có cùng tổng điểm, thứ tự xếp hạng sẽ được quyết định lần lượt theo các tiêu chí sau:

        1. So sánh thành tích của **đội vào sâu nhất** (thành tích tính theo vòng).
        2. So sánh thành tích của **đội vào sâu thứ 2** (thành tích tính theo vòng).
        3. So sánh thành tích của **đội vào sâu thứ 3** (thành tích tính theo vòng).
        4. So sánh thành tích của **đội vào sâu thứ 4** (thành tích tính theo vòng).
        5. Tổng **hiệu số** của cả 4 đội (tính cả thời gian 120 phút của trận đấu).
        6. Tổng **bàn thắng** của cả 4 đội (tính cả thời gian 120 phút của trận đấu).
        7. Nếu vẫn bằng nhau ➔ Tổng **điểm thẻ phạt** của cả 4 đội trong 120 phút thi đấu *(Thẻ đỏ = -2 điểm, Thẻ vàng = -1 điểm)*. Điểm thẻ phạt ít âm hơn sẽ xếp trên.
        8. Nếu vẫn bằng nhau ➔ **Hòa**.

        ---

        ### 💰 ĐIỀU KHOẢN CHIA THƯỞNG 
        **(Khi các vé chọn 4 đội giống nhau và đạt giải)**
        
        Trong trường hợp có nhiều vé chọn 4 đội giống nhau và đạt giải (Hạng 1, Hạng 2, Hạng 3), tiền thưởng của các hạng tương ứng sẽ được cộng gộp và chia đều cho số lượng vé đồng hạng. 
        """)