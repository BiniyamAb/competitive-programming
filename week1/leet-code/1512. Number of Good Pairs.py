def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        count = 1
        nums.sort()
        # n(n-1)/2
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                continue
            if count != 1:
                arr.append(count)
            count = 1
        
        arr.append(count)
        print(arr)
        count = 0
        for i in range(len(arr)):
            count += (arr[i] * (arr[i] - 1)) / 2

        return int(count)