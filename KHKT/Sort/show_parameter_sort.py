import matplotlib.pyplot as plt
import time
from matplotlib.ticker import MultipleLocator

# Hàm hiển thị dùng cho game
def show_parameter_sort_game(arr,highlight = [],color_highlight = [],title = '',time_show = 0):
    # Vẽ mảng lên màn hình
    plt.clf()
    plt.bar(range(len(arr)),arr,color='lightblue')

    # Đánh dấu các giá trị cần highlight theo màu
    if highlight is not None:
        for i in range(len(highlight)):
            plt.bar(highlight[i],arr[highlight[i]],color = color_highlight[i])
    
    now = time.time()
    plt.title(title+' Time: ' + str(int(now-time_show)) + 's')
    plt.pause(0.1)

# Hàm hiển thị dùng cho mảng bình thường
def show_parameter_sort(arr,highlight = [],color_highlight = [],title = '',speed = 0):
    # Vẽ mảng lên màn hình
    plt.clf()
    plt.bar(range(len(arr)),arr,color='lightblue')
    plt.grid(axis='y')

    # Đánh dấu các giá trị cần highlight
    if highlight is not None:
        for i in range(len(highlight)):
            plt.bar(highlight[i],arr[highlight[i]],color = color_highlight[i])
    
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(5))
    plt.title(title)
    plt.pause(0.1*speed)