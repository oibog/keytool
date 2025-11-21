import os
import sys
import time
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box
from colorama import init, Fore

init(autoreset=True)
console = Console()

# ==================== Banner ====================
def banner():
    print(f"""
\033[1;31m███╗   ███╗ ██████╗ ███╗   ██╗████████╗███████╗██████╗ 
\033[1;36m████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
\033[1;31m██╔████╔██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
\033[1;36m██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
\033[1;31m██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
\033[1;36m                                 Monter V16.5
       
    \033[1;36mAdmin: obi74z | YouTube: @obi74z 
    \033[1;39mTelegram: https://t.me/obi74z
    \033[1;39m> Soucre Main By: Thiệu Hoàng <        
    \033[1;33mNgày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
\033[1;39m--------------------------------------------------------
""")

# ==================== Menu ====================
def show_menu():
    table = Table(title="MENU TOOL GỘP", box=box.SQUARE_DOUBLE_HEAD, style="white")
    table.add_column("STT", style="cyan", justify="center")
    table.add_column("Tên Tool", style="magenta", justify="left")
    table.add_column("Mô Tả", style="red")
    table.add_column("Trạng Thái", style="cyan")

    table.add_row("1", "TDS FACEBOOK","COOKIE", "HOẠT ĐỘNG")
    table.add_row("2", "TTC FACEBOOK", "COOKIE", "HOẠT ĐỘNG")
    table.add_row("3", "SPAM SMS", "Tấn công số điện thoại", "HOẠT ĐỘNG")
    console.print(table)

# ==================== Kiểm tra mạng ====================
import socket
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

# ==================== Clear màn hình ====================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ==================== Main ====================
def main():
    while True:
        clear()
        banner()
        show_menu()
        kiem_tra_mang()
        try:
            choice = input(f"\n\033[1;35mNhập STT: {Fore.CYAN}").strip()
        except KeyboardInterrupt:
            console.print("\n[red]Thoát...[/]")
            break

        if choice == "1":
            code = requests.get('https://raw.githubusercontent.com/oibog/keytool/refs/heads/main/tds.py').text
            exec(code, globals())
        elif choice == "2":
            code = requests.get('https://raw.githubusercontent.com/oibog/keytool/refs/heads/main/ttc.py').text
            exec(code, globals())
        elif choice == "3":
            code = requests.get('https://raw.githubusercontent.com/oibog/keytool/refs/heads/main/sms.py').text
            exec(code, globals())
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()
