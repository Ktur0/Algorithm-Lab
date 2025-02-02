from Sort.show_parameter_sort import show_parameter_sort,show_parameter_sort_game

def heapify(arr, n, i,speed):
    largest = i      # Khởi tạo nút cha (root) là lớn nhất
    left = 2 * i + 1 # Chỉ số nút con trái
    right = 2 * i + 2 # Chỉ số nút con phải

    # Kiểm tra nếu nút con trái lớn hơn nút cha
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Kiểm tra nếu nút con phải lớn hơn nút cha
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Nếu nút cha không phải lớn nhất, hoán đổi và tiếp tục heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        show_parameter_sort(arr=arr,title="Tìm max heapify",speed=speed)
        heapify(arr, n, largest,speed)

def heap_sort(arr,speed):
    n = len(arr)

    # Xây dựng Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i,speed)

    # Trích xuất từng phần tử từ heap
    for i in range(n - 1, 0, -1):
        # Đưa phần tử lớn nhất về cuối
        arr[i], arr[0] = arr[0], arr[i]
        show_parameter_sort(arr=arr,highlight=[i],color_highlight=['red'],title='Đưa giá trị lớn nhất xuống cuối',speed=speed)
        # Giảm kích thước heap và heapify lại
        heapify(arr, i, 0,speed)


def heapify_game(arr, n, i,player,time):
    largest = i      # Khởi tạo nút cha (root) là lớn nhất
    left = 2 * i + 1 # Chỉ số nút con trái
    right = 2 * i + 2 # Chỉ số nút con phải

    # Kiểm tra nếu nút con trái lớn hơn nút cha
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Kiểm tra nếu nút con phải lớn hơn nút cha
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Nếu nút cha không phải lớn nhất, hoán đổi và tiếp tục heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        show_parameter_sort_game(arr=arr,title=player,time_show=time)
        heapify_game(arr, n, largest,player,time)

def heap_sort_game(arr,player,time):
    n = len(arr)

    # Xây dựng Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_game(arr, n, i,player,time)

    # Trích xuất từng phần tử từ heap
    for i in range(n - 1, 0, -1):
        # Đưa phần tử lớn nhất về cuối
        arr[i], arr[0] = arr[0], arr[i]
        show_parameter_sort_game(arr=arr,highlight=[i],color_highlight=['red'],title=player,time_show=time)
        # Giảm kích thước heap và heapify lại
        heapify_game(arr, i, 0,player,time)