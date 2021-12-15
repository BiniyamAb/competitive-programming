from typing import List

def kthLargestNumber(nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        nums.sort()
        return str(nums[-k])