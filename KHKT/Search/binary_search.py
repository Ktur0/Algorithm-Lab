from Search.show_parameter_search import show_parameter_search

def binary_search(arr, target,speed):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        show_parameter_search(arr=arr,highlight=[mid],highlight_color=['red'],target=str(target),speed = speed)
    return -1  # Trả về -1 nếu không tìm thấy
