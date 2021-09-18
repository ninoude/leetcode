from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        answer=[]
        nums.sort()

        for i in range(len(nums)-2):
            left, right = i+1 , len(nums)-1
            if i > 0 and nums[i] == nums[i-1]: continue
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0 and [nums[i], nums[left], nums[right]] not in answer:
                    answer.append([nums[i], nums[left], nums[right]])
                if tmp < 0:
                    left += 1
                else:
                    right -=1
        return answer

