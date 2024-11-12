import pygame
import random
import os
import sys
import time

# Thiết lập các thông số
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FONT_SIZE = 20
NUM_COLS = WIDTH // FONT_SIZE

# Khởi tạo Pygame và màn hình full-screen
pygame.init()

# Vòng lặp khởi động lại nếu chương trình bị đóng
while True:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)
    font = pygame.font.SysFont("Consolas", FONT_SIZE, bold=True)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Mảng rơi
    drops = [0] * NUM_COLS

    def matrix_effect():
        """Hiệu ứng ma trận."""
        while True:
            # Lặp qua sự kiện
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Thoát vòng lặp để khởi động lại

            # Điền màu nền đen mờ
            screen.fill((0, 0, 0, 50))

            # Vẽ hiệu ứng ma trận
            for i in range(NUM_COLS):
                char = random.choice(chars)
                color_choice = random.choices(
                    [(0, 255, 0), (255, 255, 255), (0, 255, 0, 50)], 
                    weights=[47.5, 47.5, 5], k=1
                )[0]

                # Hiển thị ký tự ma trận
                text = font.render(char, True, color_choice)
                pos_x = i * FONT_SIZE
                pos_y = drops[i] * FONT_SIZE
                screen.blit(text, (pos_x, pos_y))

                # Tăng vị trí rơi hoặc đặt lại nếu vượt chiều cao
                drops[i] = drops[i] + 1 if drops[i] * FONT_SIZE < HEIGHT else 0

            # Cập nhật màn hình
            pygame.display.flip()
            time.sleep(0.05)  # Tăng thời gian để hiệu ứng chạy chậm hơn

    # Chạy hiệu ứng ma trận
    matrix_effect()

    # Thời gian chờ để khởi động lại gần như ngay lập tức
    time.sleep(0.0001)
