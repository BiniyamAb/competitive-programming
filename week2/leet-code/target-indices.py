def targetIndices(nums, target):
    freqArr = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            freqArr.append(i)

    return freqArr