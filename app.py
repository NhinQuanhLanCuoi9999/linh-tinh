lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll = getattr, open, print, Exception, bool, input, __name__, FileNotFoundError, bytes

from requests import ConnectionError as IlIllIlllIllIl, get as IllIIlIIllIlII
from os import getenv as IIlllIIIIllIIl, system as llIIlIIlllllll
from time import sleep as lIllIIIlllIlIl
from art import text2art as lIIIlIIllIIlll
IllIIIIlIlIIllIIII = '\x1b[94m'
IllIllIIlllllllIIl = '\x1b[91m'
IllllIIlIIllIIllll = '\x1b[0m'

def lIIIlIlIIIlIlllIll():
    try:
        with llllllllllllllI('config.txt', 'r') as lllllIIIIIlIlIllIl:
            return lllllllllllllll(lllllIIIIIlIlIllIl.read(), lllllllllllllll(lllllllllllIlll, 'fromhex')('7374726970').decode())()
    except llllllllllllIII:
        return None

def IIlIIlIIIIlIllIIII(IIIIIllIIlIlIIIIII):
    with llllllllllllllI('config.txt', 'w') as lllllIIIIIlIlIllIl:
        lllllllllllllll(lllllIIIIIlIlIllIl, lllllllllllllll(lllllllllllIlll, 'fromhex')('7772697465').decode())(IIIIIllIIlIlIIIIII)

def IllllIlIIlIIIlIIII(IIIIIllIIlIlIIIIII):
    IIlIllIIllllIIlllI = f'https://api.roblox.com/users/{IIIIIllIIlIlIIIIII}'
    try:
        IIIIlIIIllIIlIIlII = IllIIlIIllIlII(IIlIllIIllllIIlllI, timeout=10)
        IIlIIlIllIIIllIIlI = IIIIlIIIllIIlIIlII.json()
        if 'isOnline' in IIlIIlIllIIIllIIlI:
            return IIlIIlIllIIIllIIlI['isOnline']
        else:
            return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    except IlIllIlllIllIl:
        lllllllllllllIl('Lỗi kết nối: Không thể kết nối đến API.')
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    except lllllllllllllII as lllIllIlIlllllIlll:
        lllllllllllllIl(f'Lỗi khi lấy dữ liệu: {lllIllIlIlllllIlll}')
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)

def IIIlllIllIlIlllIlI():
    IllllIlIIIIlllIlII = llIIlIIlllllll('ps | grep -i roblox')
    return IllllIlIIIIlllIlII == 0

def lllllIllIllIIlIIII():
    return IIlllIIIIllIIl('TERMUX_VERSION') is not None

def IIlllIIlIIlIIIIIII(IIIIIllIIlIlIIIIII, IlIIllIlllIIIlllIl):
    while llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
        if not IIIlllIllIlIlllIlI():
            lllllllllllllIl('Roblox không được mở! Mở Roblox...')
            if lllllIllIllIIlIIII():
                if lllllllllllllll(IlIIllIlllIIIlllIl, lllllllllllllll(lllllllllllIlll, 'fromhex')('73746172747377697468').decode())('http'):
                    llIIlIIlllllll(f'am start -a android.intent.action.VIEW -d "{IlIIllIlllIIIlllIl}"')
                else:
                    llIIlIIlllllll(f'am start -a android.intent.action.VIEW -d "roblox://placeID={IlIIllIlllIIIlllIl}"')
            else:
                llIIlIIlllllll('am start -n com.termux/.TermuxActivity')
        else:
            lllllllllllllIl('Roblox đang mở. Kiểm tra trạng thái...')
            if not IllllIlIIlIIIlIIII(IIIIIllIIlIlIIIIII):
                lllllllllllllIl('Đã thoát game! Đang thực hiện rejoin...')
                if lllllllllllllll(IlIIllIlllIIIlllIl, lllllllllllllll(lllllllllllIlll, 'fromhex')('73746172747377697468').decode())('http'):
                    llIIlIIlllllll(f'am start -a android.intent.action.VIEW -d "{IlIIllIlllIIIlllIl}"')
                else:
                    llIIlIIlllllll(f'am start -a android.intent.action.VIEW -d "roblox://placeID={IlIIllIlllIIIlllIl}"')
                lIllIIIlllIlIl(5)
            else:
                lllllllllllllIl('Đang trong game...')
        lIllIIIlllIlIl(10)

def IlIlllIllIIlIIIlIl():
    lllllllllllllIl('Chọn game:')
    lllllllllllllIl('1 - Blox Fruit')
    lllllllllllllIl('2 - King Legacy')
    lllllllllllllIl('3 - Meme Sea')
    lllllllllllllIl('4 - The Strongest Battleground')
    lllllllllllllIl('5 - PLS DONATE')
    lllllllllllllIl('6 - Pet Simulator')
    lllllllllllllIl('7 - Anime Defender')
    lllllllllllllIl('8 - Private Server Link')
    IllllIlIIIIIllIlIl = llllllllllllIlI('Nhập số game bạn muốn rejoin: ')
    if IllllIlIIIIIllIlIl == '1':
        return '2753915549'
    elif IllllIlIIIIIllIlIl == '2':
        return '4520749081'
    elif IllllIlIIIIIllIlIl == '3':
        return '10260193230'
    elif IllllIlIIIIIllIlIl == '4':
        return '10449761463'
    elif IllllIlIIIIIllIlIl == '5':
        return '8737602449'
    elif IllllIlIIIIIllIlIl == '6':
        return '6284583030'
    elif IllllIlIIIIIllIlIl == '7':
        return '17017769292'
    elif IllllIlIIIIIllIlIl == '8':
        return llllllllllllIlI('Nhập link Private Server: ')
    else:
        lllllllllllllIl('Lựa chọn không hợp lệ, vui lòng thử lại.')
        return IlIlllIllIIlIIIlIl()
if llllllllllllIIl == '__main__':
    lllllllllllllIl(IllIIIIlIlIIllIIII + lIIIlIIllIIlll('Linear Rejoin') + IllllIIlIIllIIllll)
    lllllllllllllIl(IllIllIIlllllllIIl + 'Bản quyền thuộc về Dawn và Linear' + IllllIIlIIllIIllll)
    IIIIIllIIlIlIIIIII = lIIIlIlIIIlIlllIll()
    if not IIIIIllIIlIlIIIIII:
        IIIIIllIIlIlIIIIII = llllllllllllIlI('Nhập user_id Roblox của bạn: ')
        IIlIIlIIIIlIllIIII(IIIIIllIIlIlIIIIII)
        lllllllllllllIl('Đã lưu user_id vào config.txt')
    IlIIllIlllIIIlllIl = IlIlllIllIIlIIIlIl()
    IIlllIIlIIlIIIIIII(IIIIIllIIlIlIIIIII, IlIIllIlllIIIlllIl)
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
    print(BLUE + text2art("Linear Rejoin") + RESET)
    print(RED + "Bản quyền thuộc về Dawn và Linear" + RESET)

    user_id = load_user_id()
    if not user_id:
        user_id = input("Nhập user_id Roblox của bạn: ")
        save_user_id(user_id)
        print("Đã lưu user_id vào config.txt")

    place_id = select_game()
    auto_rejoin(user_id, place_id)
