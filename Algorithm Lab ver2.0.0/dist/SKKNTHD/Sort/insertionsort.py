from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game

def insertion_sort(arr,speed):
    for i in range(1, len(arr)):
        key = arr[i]  # Lấy phần tử hiện tại
        j = i - 1
        show_parameter_sort(arr,highlight=[j],color_highlight=['red'],title='Chọn key',speed=speed)

        # Di chuyển các phần tử lớn hơn `key` sang phải
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            show_parameter_sort(arr,highlight=[j],color_highlight=['red'],title='Sắp xếp mảng',speed=speed)
            j -= 1
            

        # Đặt `key` vào đúng vị trí
        arr[j + 1] = key

    return arr

def insertion_sort_game(arr,player,time):
    for i in range(1, len(arr)):
        key = arr[i]  # Lấy phần tử hiện tại
        j = i - 1
        show_parameter_sort_game(arr,highlight=[j],color_highlight=['red'],title=player,time_show=time)

        # Di chuyển các phần tử lớn hơn `key` sang phải
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            show_parameter_sort_game(arr,highlight=[j],color_highlight=['red'],title=player,time_show=time)
            j -= 1
            

        # Đặt `key` vào đúng vị trí
        arr[j + 1] = key

    return arr

