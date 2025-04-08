def convert_str_to_list(line):
    arr1 = line.split(',')
    arr = []

    while '' in arr1:
        arr1.remove('')

    for i in arr1:
        arr.append(int(i))

    return arr
    
