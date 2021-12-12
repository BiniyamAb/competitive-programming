def select(arr, i):
    # code here
    minIndex = i
    for j in range(i, len(arr)):
        if arr[j] < arr[minIndex]:
            minIndex = j
    return minIndex

def selectionSort(arr, n):
    #code here
    for i in range(n):
        minIndex = select(arr, i)
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr