from typing import List

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            i = 1
            while i < len(nums):
                if nums[i] == nums[i-1]:
                    del nums[i]
                else:
                    i = i+1
            return i

