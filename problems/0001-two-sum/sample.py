#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i, x in enumerate (nums):
            if target - x in nums[i+1:]:
                return [i, nums[i+1:].index(target-x)+i+1]
