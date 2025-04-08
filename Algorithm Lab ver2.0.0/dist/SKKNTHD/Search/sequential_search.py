from Search.show_parameter_search import show_parameter_search

def sequential_search(arr,target,speed):
    
    for i in range(len(arr)):
        show_parameter_search(arr=arr,highlight=[i],highlight_color=['red'],target=target,speed = speed)
        if target == arr[i]:
            return i
    
    return -1