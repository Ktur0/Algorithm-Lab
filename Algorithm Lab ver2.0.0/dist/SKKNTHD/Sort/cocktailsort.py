from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game

def cocktail_sort(arr,speed):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        # Reset swapped để kiểm tra nếu có hoán đổi trong lần lặp này
        swapped = False

        # Lần duyệt từ trái sang phải
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                show_parameter_sort(arr=arr,highlight=[i,i+1],color_highlight=['red','red'],title='Duyệt phần tử sang phải',speed=speed)
                swapped = True

        # Nếu không có phần tử nào bị hoán đổi, danh sách đã được sắp xếp
        if not swapped:
            break

        # Giảm end vì phần tử cuối cùng đã đúng vị trí
        end -= 1

        # Lần duyệt từ phải sang trái
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                show_parameter_sort(arr=arr,highlight=[i,i+1],color_highlight=['green','green'],title='Duyệt phần tử sang trái',speed=speed)
                swapped = True

        # Tăng start vì phần tử đầu tiên đã đúng vị trí
        start += 1

    return arr

def cocktail_sort_game(arr,player,time):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        # Reset swapped để kiểm tra nếu có hoán đổi trong lần lặp này
        swapped = False

        # Lần duyệt từ trái sang phải
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                show_parameter_sort_game(arr=arr,highlight=[i,i+1],color_highlight=['red','red'],title=player,time_show=time)
                swapped = True

        # Nếu không có phần tử nào bị hoán đổi, danh sách đã được sắp xếp
        if not swapped:
            break

        # Giảm end vì phần tử cuối cùng đã đúng vị trí
        end -= 1

        # Lần duyệt từ phải sang trái
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                show_parameter_sort_game(arr=arr,highlight=[i,i+1],color_highlight=['green','green'],title=player,time_show=time)
                swapped = True

        # Tăng start vì phần tử đầu tiên đã đúng vị trí
        start += 1

    return arr