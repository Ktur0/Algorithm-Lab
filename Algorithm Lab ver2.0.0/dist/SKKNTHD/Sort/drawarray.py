import pygame

def draw_array(array, limit, WIDTH, HEIGHT, screen):
    pygame.font.init()  # Initialize the font module
    font = pygame.font.SysFont('Arial', 18)  # Create a font object

    drawing_width = WIDTH - 2 * limit  # Chiều rộng vẽ (trừ khoảng cách biên)
    bar_width = drawing_width // len(array)  # Độ rộng của mỗi cột
    for i, value in enumerate(array):
        x = limit + i * bar_width  # Tọa độ x, bắt đầu từ biên trái
        y = HEIGHT - value  # Chiều cao từ dưới lên
        pygame.draw.rect(screen, (30, 255, 217), (x, y, bar_width - 2, value))  # Vẽ cột (2 pixel khoảng cách giữa các cột)
        
        # Render the value as text
        text_surface = font.render(str(value), True, (0, 0, 00))
        text_rect = text_surface.get_rect(center=(x + bar_width // 2, y - 10))  # Center the text above the column
        screen.blit(text_surface, text_rect)  # Blit the text onto the screen

    pygame.display.flip()  # Cập nhật màn hình