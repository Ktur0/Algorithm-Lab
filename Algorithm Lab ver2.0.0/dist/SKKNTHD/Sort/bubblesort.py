from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game

def bubble_sort_game(arr,player,time):
    n = len(arr)
    # Lặp qua từng phần tử của mảng
    for i in range(n):
        # Cờ hiệu để kiểm tra nếu mảng đã được sắp xếp
        swapped = False
        show_parameter_sort_game(arr,title=player,time_show= time)
        # So sánh các phần tử liên tiếp và hoán đổi nếu cần thiết
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                show_parameter_sort_game(arr,highlight=[j,j+1],color_highlight=['red','red'],title=player ,time_show= time)
        # Nếu không có hoán đổi nào xảy ra, mảng đã được sắp xếp
        if not swapped:
            break
    return arr

def bubble_sort(arr,speed):
    n = len(arr)
    # Lặp qua từng phần tử của mảng
    for i in range(n):
        # Cờ hiệu để kiểm tra nếu mảng đã được sắp xếp
        swapped = False
        show_parameter_sort(arr,title='Bắt đầu lặp lần thứ: '+  str(i),speed=speed)
        # So sánh các phần tử liên tiếp và hoán đổi nếu cần thiết
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                show_parameter_sort(arr,highlight=[j,j+1],color_highlight=['red','red'],title='Hoán đổi vị trí',speed=speed)
        # Nếu không có hoán đổi nào xảy ra, mảng đã được sắp xếp
        if not swapped:
            break
    return arr