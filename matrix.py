import random
import time
import os

def matrix_effect():
    width = os.get_terminal_size().columns
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Tạo mảng với độ dài là chiều rộng của màn hình terminal
    drops = [0] * width

    while True:
        for i in range(width):
            # Xác định ký tự và màu ngẫu nhiên
            char = random.choice(chars)
            # Chọn màu với tần suất 5% cho khung xanh lá, còn lại chia đều cho trắng và xanh lá
            color = random.choices(
                ["\033[0;32m", "\033[1;37m", "\033[0;32;42m"],
                weights=[47.5, 47.5, 5],  # 47.5% xanh lá, 47.5% trắng, 5% khung xanh lá
                k=1
            )[0]

            if drops[i] == 0 and random.random() > 0.975:
                drops[i] = random.randint(1, os.get_terminal_size().lines)

            # In ký tự ngẫu nhiên nếu vị trí "rơi" chưa tới cuối
            if drops[i] > 0:
                print(f"{color}{char}\033[0m", end="")
                drops[i] -= 1
            else:
                print(" ", end="")  # In khoảng trắng nếu không hiển thị ký tự mới
        print()
        time.sleep(0.001)

try:
    matrix_effect()
except KeyboardInterrupt:
    print("\nMatrix effect stopped.")
