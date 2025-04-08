from Search.show_parameter_search import show_parameter_search

def interpolation_search(arr, target,speed):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        show_parameter_search(arr=arr,highlight=[low,high],highlight_color=['yellow','yellow'],target=target,speed = speed)
        # Ước lượng vị trí
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        show_parameter_search(arr=arr,highlight=[low,high,pos],highlight_color=['yellow','yellow','red'],target=target,speed = speed)
        # Nếu tìm thấy
        if arr[pos] == target:
            return pos
        
        # Nếu giá trị ở vị trí ước lượng nhỏ hơn target
        if arr[pos] < target:
            low = pos + 1
        
        # Nếu giá trị ở vị trí ước lượng lớn hơn target
        else:
            high = pos - 1

    return -1  # Không tìm thấy
