# Chỉ lấy đoạn banner + thongtin + thông báo "Ấn 1 để thoát" (thongtin màu trắng, nút 1 màu đỏ)

from time import sleep
import sys

# nếu bạn đã import Colorate, Colors từ pystyle ở phần khác thì không cần import lại
# from pystyle import Colorate, Colors

banners = f"""
╔═════════════════════════════════════════════════════════════════
███╗   ███╗ ██████╗ ███╗   ██╗████████╗███████╗██████╗ 
████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
╠═════════════════════════════════════════════════════════════════
║- Admin : obi74z
║- Youtube : https://www.youtube.com/@cobi74z
╚═════════════════════════════════════════════════════════════════
"""

# Thông tin (in màu trắng)
thongtin = """
- TOOL ĐÃ CÓ UPDATE V1.5 VUI LÒNG TẢI BẢN MỚI NHẤT !!!
- ẤN PHÍM "1" ĐỂ OUT TOOL

"""

def banner():
    # in banner bằng Colorate nếu bạn đã import Colorate, Colors; nếu không, fallback ra ANSI trắng cho thongtin
    try:
        from pystyle import Colorate, Colors
        print(Colorate.Horizontal(Colors.green_to_yellow, banners))
        # in thongtin màu trắng bằng ANSI (đảm bảo hiển thị trắng)
        print("\033[1;37m" + thongtin + "\033[0m")
    except Exception:
        # nếu không có pustyle thì in bình thường (thongtin trắng bằng ANSI)
        print(banners)
        print("\033[1;37m" + thongtin + "\033[0m")

# Gọi banner
banner()



# Vòng chờ nhập '1' để thoát (prompt màu đỏ)
while True:
    try:
        lua_chon = input("\033[1;31m- Nhập lựa chọn: \033[0m").strip()  # prompt đỏ
        if lua_chon == "1":
            print("\033[1;31m- Đã thoát tool.\033[0m")  # thông báo thoát màu đỏ
            sys.exit()
        else:
            print("\033[1;31m- Vui lòng chỉ nhập '1' để thoát.\033[0m")
            sleep(0.3)
    except KeyboardInterrupt:
        # chặn Ctrl+C, nhắc người dùng dùng '1'
        print("\n\033[1;31m- Không dùng Ctrl+C — hãy nhập '1' để thoát.\033[0m")


