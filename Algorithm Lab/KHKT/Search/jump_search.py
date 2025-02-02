import math
from Search.show_parameter_search import show_parameter_search

def jump_search(arr, target,speed):
    n = len(arr)
    step = int(math.sqrt(n))  # Kích thước bước nhảy
    prev = 0

    # Nhảy qua các khối
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        show_parameter_search(arr=arr,highlight=[prev],highlight_color=['red'],target=target,speed = speed)
        if prev >= n:
            return -1  # Không tìm thấy

    # Linear Search trong khối đã tìm được
    while prev < min(step, n):
        show_parameter_search(arr=arr,highlight=[prev-1,step],highlight_color=['orange','red'],target=target,speed = speed)
        if arr[prev] == target:
            return prev
        prev += 1

    return -1  # Không tìm thấy

