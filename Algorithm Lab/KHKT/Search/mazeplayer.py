import pygame
import random
import sys
import time

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ (cố định, nhưng kích thước mê cung có thể thay đổi)
WINDOW_WIDTH, WINDOW_HEIGHT = 1067, 600

# Background
finding_gameplay_player = pygame.image.load('KHKT/Image/finding_gameplay_player.jpg')

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Hướng di chuyển (delta row, delta col)
DIRECTIONS = [
    (-1, 0),  # Lên
    (1, 0),   # Xuống
    (0, -1),  # Trái
    (0, 1),   # Phải
]
def create_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    return maze
def generate_maze(maze, start_row, start_col):
    maze[start_row][start_col] = 0
    stack = [(start_row, start_col)]

    while stack:
        current_row, current_col = stack[-1]
        neighbors = []

        for dr, dc in DIRECTIONS:
            nr, nc = current_row + 2 * dr, current_col + 2 * dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 1:
                neighbors.append((nr, nc))

        if neighbors:
            next_row, next_col = random.choice(neighbors)
            wall_row = current_row + (next_row - current_row) // 2
            wall_col = current_col + (next_col - current_col) // 2
            maze[wall_row][wall_col] = 0
            maze[next_row][next_col] = 0
            stack.append((next_row, next_col))
        else:
            stack.pop()
def draw_maze(screen, maze, cell_size):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(
                screen,
                color,
                (col * cell_size, row * cell_size, cell_size, cell_size),
            )
def finding_game_player():
    # Kích thước mê cung
    rows, cols = 21, 21  # Phải là số lẻ để đường đi được kết nối
    cell_size = min(WINDOW_WIDTH // cols, WINDOW_HEIGHT // rows)

    # Tạo mê cung
    maze = create_maze(rows, cols)
    generate_maze(maze, 0, 0)  # Bắt đầu từ ô (0, 0)

    # Biến đếm số bước đi trong mê cung và thông báo kết quả
    result = 'You Win!'
    steps = 0

    # Biến đếm thời gian
    time_start = time.time()

    # Vị trí người chơi và điểm đích
    player_pos = [0, 0]
    end_pos = [rows - 1, cols - 1]

    # Khởi tạo màn hình (làm một lần)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True

    while running:
        # Tô lại nền (tránh màn hình bị giật)
        screen.blit(finding_gameplay_player, (0, 0))

        # Thời gian chơi
        time_now = str(int(time.time() - time_start)) + 's'

        # Hiển thị thời gian và số bước lên màn hình
        font = pygame.font.Font('KHKT/Font/ClearSans-Bold.ttf',60)
        text_steps = font.render(str(steps), True, GREEN)
        text_time = font.render(time_now, True, RED)

        screen.blit(text_steps, (820, 150))
        screen.blit(text_time, (820, 260))

        # Vẽ mê cung
        draw_maze(screen, maze, cell_size)

        # Vẽ người chơi
        pygame.draw.rect(
            screen,
            GREEN,
            (
                player_pos[1] * cell_size + 5,
                player_pos[0] * cell_size + 5,
                cell_size - 10,
                cell_size - 10,
            ),
        )

        # Vẽ điểm đích
        pygame.draw.rect(
            screen,
            RED,
            (
                end_pos[1] * cell_size + 5,
                end_pos[0] * cell_size + 5,
                cell_size - 10,
                cell_size - 10,
            ),
        )

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                dr, dc = 0, 0
                if event.key == pygame.K_UP:
                    dr, dc = -1, 0
                    steps += 1
                elif event.key == pygame.K_DOWN:
                    dr, dc = 1, 0
                    steps += 1
                elif event.key == pygame.K_LEFT:
                    dr, dc = 0, -1
                    steps += 1
                elif event.key == pygame.K_RIGHT:
                    dr, dc = 0, 1
                    steps += 1

                new_row = player_pos[0] + dr
                new_col = player_pos[1] + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                    player_pos = [new_row, new_col]

        # Kiểm tra thắng
        if player_pos == end_pos:
            running = False

        # Cập nhật màn hình sau khi vẽ xong
        pygame.display.flip()
        clock.tick(FPS)

    return steps, time_now


