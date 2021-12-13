def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    majorityElements = []
    n_3 = len(nums)//3
    nums.sort()

    count=1
    num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count+=1
            continue
        else:
            if count > n_3:
                majorityElements.append(num)
            count = 1
            num = nums[i]
    
    if count > n_3:
        majorityElements.append(num)

    return majorityElements
    


print(majorityElement([3,2,3]))
