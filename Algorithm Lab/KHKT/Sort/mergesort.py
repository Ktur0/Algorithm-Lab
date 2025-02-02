from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game

def merge_sort(arr,speed):
    if len(arr) <= 1:
        return arr

    # Chia mảng thành hai nửa
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid],speed=speed)
    right_half = merge_sort(arr[mid:],speed=speed)

    # Kết hợp hai nửa đã sắp xếp
    return merge(left_half, right_half,speed=speed)

def merge(left, right,speed):
    sorted_array = []
    i = j = 0

    # So sánh và gộp hai mảng con đã sắp xếp
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            show_parameter_sort(arr=left,highlight=[i],color_highlight=['lightblue'],speed=speed)
            i += 1
            
        else:
            sorted_array.append(right[j])
            show_parameter_sort(arr=right,highlight=[j],color_highlight=['lightblue'],speed=speed)
            j += 1

    # Thêm các phần tử còn lại của mảng con
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    show_parameter_sort(arr=sorted_array,speed=speed)

    return sorted_array


def merge_sort_game(arr,player,time):
    if len(arr) <= 1:
        return arr

    # Chia mảng thành hai nửa
    mid = len(arr) // 2
    left_half = merge_sort_game(arr[:mid],player,time)
    right_half = merge_sort_game(arr[mid:],player,time)

    # Kết hợp hai nửa đã sắp xếp
    return merge_game(left_half, right_half,player,time)

def merge_game(left, right,player,time):
    sorted_array = []
    i = j = 0

    # So sánh và gộp hai mảng con đã sắp xếp
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            show_parameter_sort_game(arr=left,highlight=[i],color_highlight=['lightblue'],title=player,time_show=time)
            i += 1
            
        else:
            sorted_array.append(right[j])
            show_parameter_sort_game(arr=right,highlight=[j],color_highlight=['lightblue'],title=player,time_show=time)
            j += 1

    # Thêm các phần tử còn lại của mảng con
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    show_parameter_sort_game(arr=sorted_array,title=player,time_show=time)

    return sorted_array