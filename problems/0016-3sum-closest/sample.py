from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0
        answer = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums)-2):
            left, right = i+1 , len(nums)-1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if abs(tmp - target) < abs(answer - target):
                    answer = tmp
                if tmp < target:
                    left += 1
                else:
                    right -=1

        return answer
