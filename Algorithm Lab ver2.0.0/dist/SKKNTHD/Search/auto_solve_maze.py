import pygame
import random
import sys

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)  # Màu cho các ô đang được thăm
GRAY = (200, 200, 200)  # Màu nút
DARK_GRAY = (100, 100, 100)

# Biến tốc độ (thời gian chờ giữa mỗi bước, tính bằng ms)
DRAW_SPEED = 60  # Thay đổi giá trị này để điều chỉnh tốc độ

pygame.init()

# Đặt kích thước cửa sổ
window_width = 1067
window_height = 600

# Đặt kích thước mê cung (số hàng và cột phải là số lẻ)
rows = 26  # Thay đổi kích thước mê cung tại đây
cols = 26  # Thay đổi kích thước mê cung tại đây

# Kích thước mỗi ô vuông trong mê cung
CELL_SIZE = 23

# Font chữ
number_message_font = pygame.font.Font('SKKNTHD/Font/ClearSans-Bold.ttf',40)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Maze Solver with Button")
run = True
box = pygame.Rect(100,100,50,50)
solving = False
x_mouse,y_mouse = 0,0
mouse_box = pygame.Rect(x_mouse,y_mouse,20,20)


def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]  # Bắt đầu với toàn tường
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]

    def carve_passages(x, y):
        visited[x][y] = True
        maze[x][y] = 0  # Biến ô này thành đường đi

        # Ngẫu nhiên hóa thứ tự di chuyển
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Nhảy 2 ô (đảm bảo có tường ngăn)
            if is_valid(nx, ny):
                # Mở tường giữa hai ô
                maze[x + dx][y + dy] = 0
                carve_passages(nx, ny)

    carve_passages(0, 0)
    return maze


def random_end(maze):
    rows, cols = len(maze), len(maze[0])
    while True:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if maze[x][y] == 0:  # Điểm kết thúc phải nằm trên đường đi
            return (x, y)


def draw_maze(screen, maze, path, start, end, visited):
    rows, cols = len(maze), len(maze[0])

    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 1:
                color = BLACK  # Tường
            elif (x, y) in path:
                color = BLUE  # Đường đi
            elif visited[x][y]:
                color = YELLOW  # Đang thăm
            else:
                color = WHITE  # Đường trống
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Vẽ điểm bắt đầu
    sx, sy = start
    pygame.draw.rect(screen, GREEN, (sy * CELL_SIZE, sx * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Vẽ điểm kết thúc
    ex, ey = end
    pygame.draw.rect(screen, RED, (ey * CELL_SIZE, ex * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def dfs_maze(screen, maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def dfs(x, y):
        if (x, y) == end:
            path.append((x, y))
            return True

        if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == 1 or visited[x][y]:
            return False

        visited[x][y] = True

        # Hiển thị trạng thái động
        draw_maze(screen, maze, path, start, end, visited)
        pygame.display.flip()
        pygame.time.delay(DRAW_SPEED)  # Sử dụng biến tốc độ để điều chỉnh

        path.append((x, y))

        if dfs(x - 1, y):  # Lên
            return True
        if dfs(x + 1, y):  # Xuống
            return True
        if dfs(x, y - 1):  # Trái
            return True
        if dfs(x, y + 1):  # Phải
            return True

        path.pop()
        return False

    dfs(*start)
    return path

end = ''

def findinggame(maze,start,end):
    
    start_text = number_message_font.render(str(start),True,('green'))
    end_text = number_message_font.render(str(end),True,('red'))

    screen.blit(start_text,(815,155))
    screen.blit(end_text,(815,235))
    dfs_maze(screen, maze, start, end)
