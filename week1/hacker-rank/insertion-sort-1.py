def insertionSort1(n, arr):
    def print_arr(array):
        for i in arr:
            print(i, end=' ')
        print()

    num = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if(num < arr[i]):
            arr[i + 1] = arr[i]
            print_arr(arr)
            continue
        arr[i + 1] = num
        break
    
    if arr[0] == arr[1]:
        arr[0] = num

    print_arr(arr)
    return


