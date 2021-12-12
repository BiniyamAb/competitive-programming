def sortColors(nums):
    def select(arr, i):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        return minIndex

    for i in range(len(nums)):
        minIndex = select(nums, i)
        nums[i], nums[minIndex] = nums[minIndex], nums[i]

