# Kramer/Specter Deobf by KhanhNguyen9872
# file name: [ToolGop.py] (py - 3.11)
# dump -> code 51
import threading,base64
import os,time,re,json,random
from datetime import datetime, timedelta
from time import sleep,strftime
from bs4 import BeautifulSoup
import requests
import os, sys
import socket

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip3 install requests pysocks")
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""


\033[1;31m███╗   ███╗ ██████╗ ███╗   ██╗████████╗███████╗██████╗ 
\033[1;36m████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
\033[1;31m██╔████╔██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
\033[1;36m██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
\033[1;31m██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
\033[1;36m   

\033[1;31m                                       © MONTER V1.6

\033[1;33m==========================================================
[⟨⟩] \033[1;31m➩ \033[1;31mAdmin: \033[1;34mobi74z
[⟨⟩] \033[1;31m➩ \033[1;34mTelegram \033[1;39mhttps://t.me/obi74z
[⟨⟩] \033[1;31m➩ \033[1;34mGiới hạn thiết bị : \033[1;32m1/*
\033[1;33m==========================================================
\033[1;34m                -UPDATE V1.6-
\033[1;36m[⟨⟩]➩ \033[1;34mNEW UPDATE V1.6
\033[1;36m[⟨⟩]➩ \033[1;34mUPDATE GIAO DIỆN
\033[1;36m[⟨⟩]➩ \033[1;34mUPDATE TOOL
\033[1;36m[⟨⟩]➩ \033[1;34mFIX DELAY
\033[1;36m[⟨⟩]➩ \033[1;34mFIX CRACK KEY  
\033[1;33m==========================================================
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.0001)
def bes4(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)
    
    # Nếu yêu cầu thành công (status code 200)
    if response.status_code == 200:
        # Phân tích nội dung HTML của trang web
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm thẻ <span> chứa thông tin phiên bản và trạng thái bảo trì
        version_tag = soup.find('span', id='version0')
        maintenance_tag = soup.find('span', id='maintenance0')
        
        # Lấy nội dung văn bản bên trong thẻ
        version = version_tag.text.strip() if version_tag else None
        maintenance = maintenance_tag.text.strip() if maintenance_tag else None
        
        return version, maintenance
    
    return None, None

def checkver():
    url = 'https://key.c25tool.net/'
    version, maintenance = bes4(url)
    
    if maintenance == 'on':
        print("Tool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm Tele: https://t.me/off")
        sys.exit()
    
    return version

# Sử dụng hàm checkver để kiểm tra phiên bản
current_version = checkver()
if current_version:
  
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
# Hàm để lấy địa chỉ IP của thiết bị
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return None

# Hàm để hiển thị địa chỉ IP của thiết bị
def display_ip_address(ip_address):
    if ip_address:
        banner = """
\033[1;31m███╗   ███╗ ██████╗ ███╗   ██╗████████╗███████╗██████╗ 
\033[1;36m████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
\033[1;31m██╔████╔██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
\033[1;36m██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
\033[1;31m██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
\033[1;36m
                                                
\033[1;31m                                       © MONTER V1.6

\033[1;33m==========================================================
[⟨⟩] \033[1;31m➩ \033[1;31mAdmin: \033[1;34mobi74z
[⟨⟩] \033[1;31m➩ \033[1;34mTelegram \033[1;39mhttps://t.me/obi74z
[⟨⟩] \033[1;31m➩ \033[1;34mGiới hạn thiết bị : \033[1;32m1/*
\033[1;33m==========================================================
\033[1;34m                -UPDATE V1.6-
\033[1;36m[⟨⟩]➩ \033[1;34mNEW UPDATE V1.6
\033[1;36m[⟨⟩]➩ \033[1;34mUPDATE GIAO DIỆN
\033[1;36m[⟨⟩]➩ \033[1;34mUPDATE TOOL
\033[1;36m[⟨⟩]➩ \033[1;34mFIX DELAY
\033[1;36m[⟨⟩]➩ \033[1;34mFIX CRACK KEY
\033[1;33m==========================================================
"""

        os.system('cls' if os.name == 'nt' else 'clear')
        for x in banner:
            print(x, end="")
            time.sleep(0.001)

        print(f"\033[1;32mĐịa chỉ IP : {ip_address}     Version: V1.6")  # {current_version}
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

# Hàm để lưu thông tin IP và key vào tệp tin JSON
def luu_thong_tin_ip(ip, key, expiration_date):
    data = {}
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    # Lưu key cho IP vào trong dữ liệu
    data[ip] = {'key': key, 'expiration_date': expiration_date.isoformat()}

    # Lưu lại vào tệp tin
    with open('ip_key.json', 'w') as file:
        json.dump(data, file)

# Hàm để kiểm tra xem IP đã sử dụng key chưa và key còn hạn hay không
def kiem_tra_ip(ip):
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
            if ip in data:
                expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
                if expiration_date > datetime.now():
                    return data[ip]['key']
            return None
    except (FileNotFoundError, KeyError, TypeError):
        return None

# Hàm để tạo key và URL mới dựa trên IP hiện tại
def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
 #   keyvip=("ntoolvip")
    
    # Xử lý địa chỉ IP để chỉ lấy các số
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
        
    key = f'NTOOL-{key1}{ip_numbers}'
    # Thời gian hết hạn là 23:59:00 hôm nay
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://key.c25tool.net/key.html?key={key}'
    return url, key, expiration_date

# Hàm để kiểm tra xem đã qua 00:00:01 của ngày mới chưa
def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    start_new_day = midnight + timedelta(seconds=1)
    return now >= start_new_day
# Chương trình chính
def main():
    # Lấy và hiển thị địa chỉ IP của thiết bị
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    # Kiểm tra và tạo link rút gọn để vượt key cho từng địa chỉ IP
    if ip_address:
        existing_key = True
        if existing_key==True:
            print(f"\033[1;35mCHECKING KEY..... ")
            sleep(2)
        else:
            url, key, expiration_date = generate_key_and_url(ip_address)
            token_yeumoney = '432c9b236e4e2a7ca16f55b2029fe3461c78be79bb267c98e4f80f49303dbab3'
            yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
            if yeumoney_response.status_code == 200:
                yeumoney_data = yeumoney_response.json()
                if yeumoney_data.get('status') == "error":
                    print(yeumoney_data.get('message'))
                    quit()
                else:
                    link_key = yeumoney_data.get('shortenedUrl')
                    token_link4m = '6671b20e704d5f32b2048914'
                    link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key}')
                    print("\033[1;31mLưu Ý: \033[1;33mTool Free \033[1;91m❣\033[1;32m")
                    # Kiểm tra kết quả trả về từ link rút gọn
                    if link4m_response.status_code == 200:
                        link4m_data = link4m_response.json()
                        if link4m_data.get('status') == "error":
                            print(link4m_data.get('message'))
                            quit()
                        else:
                            link_key = link4m_data.get('shortenedUrl')
                            print('Link Để Vượt Key Là:', link_key)  # Sử dụng dấu phẩy thay vì dấu cộng
                    else:
                        print('Không thể kết nối đến dịch vụ rút gọn URL')
                        quit()
            else:
                print('Không thể kết nối đến dịch vụ rút gọn URL')
                quit()

            # Yêu cầu người dùng nhập key
            while True:
                keynhap = input('Key Đã Vượt Là: ')

                # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                if keynhap == key:
                    print('Key Đúng Mời Bạn Dùng Tool')
                    sleep(2)
                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                    break
                else:
                    print('Key Sai Vui Lòng Vượt Lại Link:', link_key)
        
        # Kiểm tra nếu đã qua 00:00:01 của ngày mới
        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới

if __name__ == "__main__":
    main()
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mTool TTC Facebook \033[0;31m[Offline]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tiện Ích \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3 \033[1;97m: \033[1;34mTool Get ID Facebook \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Linh Tinh\033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4 \033[1;97m: \033[1;34mBumx \033[1;32m[Online] [HOT] ")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1':
		# Thành Công
		exec(requests.get('erorr').text)
	elif chon == '2':
		exec(requests.get('https://raw.githubusercontent.com/oibog/keytool/refs/heads/main/tds.py').text)
	elif chon == '3':
		exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/main/GETUID.py').text)
	elif chon == '4':
	    exec(requests.get('https://raw.githubusercontent.com/oibog/keytool/refs/heads/main/bumx.py').text)
	else:
		sys.exit("")
