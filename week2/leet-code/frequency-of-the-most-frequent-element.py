import math
from typing import List
def average_calc(dict3):
    sum = 0
    for _, v in dict3.items():
        sum+=v
    return math.ceil(sum / len(dict3))

def maxFrequency(nums: List[int], k: int) -> int:
    nums.sort()
    countFreq = 1
    dict1 = {}
    dict2 ={}
    frequencies = []

    for i in range(len(nums)):
        dict1[nums[i]] = dict1.get(nums[i], 0) + 1
    print(dict1)
    average_freq = average_calc(dict1)
    print(average_freq)
    if average_freq == 0 or average_freq == 1:
        dict2 = {nums[-1]: len(nums) - 1}
    else:
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                countFreq+=1
                continue
            if countFreq >= average_freq:
                dict2[nums[i - 1]] = i - 1
                countFreq = 1

    print(dict2)
    for key, v in dict2.items():
        freq = 1
        count = 0
        for i in range(v -1, -1, -1):
            if (count + (key -nums[i])) > k:
                break
            count+=key - nums[i]
            freq+=1

        if freq == 19:
            print(key)

        frequencies.append(freq)

    return max(frequencies)

# print(maxFrequency([1,2,4], 5))
# print(maxFrequency([1,4,8,13], 5))
# print(maxFrequency([3,9,6,5,3], 2))
# print(maxFrequency([9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966],
# 3056))
print(maxFrequency([9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997]
,7925))





