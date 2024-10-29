import requests
import time
import os
from art import text2art

# Mã ANSI cho màu xanh và màu đỏ
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

def load_user_id():
    try:
        with open("config.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def save_user_id(user_id):
    with open("config.txt", "w") as file:
        file.write(user_id)

def check_user_status(user_id):
    api_url = f'https://api.roblox.com/users/{user_id}'
    try:
        response = requests.get(api_url, timeout=10)  # Thêm timeout
        data = response.json()
        if 'isOnline' in data:
            return data['isOnline']
        else:
            return False
    except requests.ConnectionError:
        print("Lỗi kết nối: Không thể kết nối đến API.")
        return False
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")
        return False

def is_roblox_open():
    # Kiểm tra xem Roblox có đang chạy hay không
    result = os.system("ps | grep -i roblox")  # Kiểm tra process trên hệ thống
    return result == 0  # Trả về True nếu Roblox đang chạy

def is_termux_running():
    # Kiểm tra xem mã có đang chạy trong Termux hay không
    return os.getenv('TERMUX_VERSION') is not None

def auto_rejoin(user_id, place_id):
    while True:
        if not is_roblox_open():
            print("Roblox không được mở! Mở Roblox...")
            if is_termux_running():
                # Nếu đang ở trong Termux, chỉ cần mở Roblox
                if place_id.startswith("http"):
                    os.system(f'am start -a android.intent.action.VIEW -d "{place_id}"')
                else:
                    os.system(f'am start -a android.intent.action.VIEW -d "roblox://placeID={place_id}"')
            else:
                # Nếu không ở trong Termux, mở Termux
                os.system("am start -n com.termux/.TermuxActivity")
        else:
            print("Roblox đang mở. Kiểm tra trạng thái...")
            if not check_user_status(user_id):
                print("Đã thoát game! Đang thực hiện rejoin...")
                if place_id.startswith("http"):
                    os.system(f'am start -a android.intent.action.VIEW -d "{place_id}"')
                else:
                    os.system(f'am start -a android.intent.action.VIEW -d "roblox://placeID={place_id}"')
                time.sleep(5)  # Thời gian chờ trước khi kiểm tra lại
            else:
                print("Đang trong game...")

        time.sleep(10)  # Thời gian chờ trước khi kiểm tra lại

def select_game():
    print("Chọn game:")
    print("1 - Blox Fruit")
    print("2 - King Legacy")
    print("3 - Meme Sea")
    print("4 - The Strongest Battleground")
    print("5 - PLS DONATE")
    print("6 - Pet Simulator")
    print("7 - Anime Defender")
    print("8 - Private Server Link")

    choice = input("Nhập số game bạn muốn rejoin: ")
    if choice == '1':
        return "2753915549"
    elif choice == '2':
        return "4520749081"
    elif choice == '3':
        return "10260193230"
    elif choice == '4':
        return "10449761463"
    elif choice == '5':
        return "8737602449"
    elif choice == '6':
        return "6284583030"
    elif choice == '7':
        return "17017769292"
    elif choice == '8':
        return input("Nhập link Private Server: ")
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
        return select_game()

if __name__ == "__main__":
    print(BLUE + text2art("Linear Rejoin 1.0") + RESET)
    print(RED + "Bản quyền thuộc về Dawn và Linear" + RESET)

    user_id = load_user_id()
    if not user_id:
        user_id = input("Nhập user_id Roblox của bạn: ")
        save_user_id(user_id)
        print("Đã lưu user_id vào config.txt")

    place_id = select_game()
    auto_rejoin(user_id, place_id)
