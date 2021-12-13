def largestNumber(nums):
    # these only works in python2
    """
    :type nums: List[int]
    :rtype: str
    """
    zeros = True
    for val in nums:
        if val != 0:
            zeros = False
            break
    if zeros == True:
        return "0"
    else:
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        nums = "".join(nums)

        return nums