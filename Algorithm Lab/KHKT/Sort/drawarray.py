import pygame

def draw_array(array,limit,WIDTH,HEIGHT,screen):
    drawing_width = WIDTH - 2 * limit  # Chiều rộng vẽ (trừ khoảng cách biên)
    bar_width = drawing_width // len(array)  # Độ rộng của mỗi cột
    for i, value in enumerate(array):
        x = limit + i * bar_width  # Tọa độ x, bắt đầu từ biên trái
        y = HEIGHT - value  # Chiều cao từ dưới lên
        pygame.draw.rect(screen, (30, 255, 217), (x, y, bar_width - 2, value))  # Vẽ cột (2 pixel khoảng cách giữa các cột)
    pygame.display.flip()  # Cập nhật màn hình