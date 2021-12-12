def countingSort(arr):
    frequencyArr = [0] * 100
    for i in range(len(arr)):
        frequencyArr[arr[i]]+=1

    return frequencyArr

