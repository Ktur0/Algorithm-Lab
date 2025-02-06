from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game
    
def quick_sort(arr, low, high,speed):
    if low < high:
        # Chọn pivot và chia mảng
        pivot_index = partition(arr, low, high,speed)

        # Gọi đệ quy cho mảng con bên trái và bên phải của pivot
        quick_sort(arr, low, pivot_index - 1,speed=speed)
        quick_sort(arr, pivot_index + 1, high,speed=speed)

def partition(arr, low, high,speed):
    # Chọn phần tử cuối cùng làm pivot
    pivot = arr[high]
    i = low - 1  # Con trỏ cho phần tử nhỏ hơn pivot

    show_parameter_sort(arr,highlight=[high],color_highlight=['red'],title = "Chọn pivot",speed=speed)

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Hoán đổi nếu phần tử nhỏ hơn hoặc bằng pivot
            arr[i], arr[j] = arr[j], arr[i]
            show_parameter_sort(arr,highlight=[high,i,j],color_highlight=['red','yellow','green'],title="Hoán đổi vị trí",speed=speed)

    # Đưa pivot vào đúng vị trí
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    show_parameter_sort(arr,highlight=[i+1],color_highlight=['red'],title="Pivot ở đúng vị trí",speed=speed)
    return i + 1

def quick_sort_game(arr, low, high,player,time):
    if low < high:
        # Chọn pivot và chia mảng
        pivot_index = partition_game(arr, low, high,player,time)

        # Gọi đệ quy cho mảng con bên trái và bên phải của pivot
        quick_sort_game(arr, low, pivot_index - 1,player,time)
        quick_sort_game(arr, pivot_index + 1, high,player,time)

def partition_game(arr,low,high,player,time):
    # Chọn phần tử cuối cùng làm pivot
    pivot = arr[high]
    i = low - 1  # Con trỏ cho phần tử nhỏ hơn pivot

    show_parameter_sort_game(arr,highlight=[high],color_highlight=['red'],title = player ,time_show=time)

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Hoán đổi nếu phần tử nhỏ hơn hoặc bằng pivot
            arr[i], arr[j] = arr[j], arr[i]
            show_parameter_sort_game(arr,highlight=[high,i,j],color_highlight=['red','yellow','green'],title= player ,time_show = time)

    # Đưa pivot vào đúng vị trí
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    show_parameter_sort_game(arr,highlight=[i+1],color_highlight=['red'],title=player,time_show = time)
    return i + 1