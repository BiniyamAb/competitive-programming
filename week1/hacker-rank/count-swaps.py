def countSwaps(a):
    totalSwaps = 0
    tempSwaps = -1
    for i in range(len(a)):
        if tempSwaps == 0:
            print("Array is sorted in", totalSwaps, "swaps.")
            print("First Element:", a[0])
            print("Last Element:", a[len(a) - 1])
            return
        tempSwaps = 0
        for j in range(len(a) - 1):
            if(a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                totalSwaps += 1
                tempSwaps += 1

    print("Array is sorted in", totalSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a) - 1])

    return

countSwaps([6, 4, 1])