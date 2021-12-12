def smallerNumbersThanCurrent(nums):
    nums2 = nums[:]
    nums2.sort()


    arr = []
    for i in range(len(nums)):
        for j in range(len(nums2)):
            if nums[i] == nums2[j]:
                freq = len(nums2) - (len(nums2) - j)
                arr.append(freq)
                break

    return arr
