#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            output = []
            if ((target - nums[i]) in nums and nums.index(target - nums[i]) > i):
                output.append(i)
                output.append(nums.index(target - nums[i]))
                print(output)
        return output

#nums1 = [2,7,11,15]
#target1 = 9
#nums2 = [3,2,4]
#target2 = 6
nums = [2,7,11,15]
target = 9
instance = Solution()
print(instance.twoSum(nums, target))
