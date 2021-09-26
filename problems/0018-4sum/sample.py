from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(nums)
        n = len(nums)
        if n < 4: return []
        answer = []

        for i in range(n-3):
            if 0 < i < n-3 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                left = j+1
                right = n-1
                if i+1 < j < n-2 and nums[j] == nums[j-1]:
                    continue
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < n-1 and nums[left] == nums[left+1]:
                            left += 1
                        while right > 0 and nums[right] == nums[right-1]:
                            right -= 1
                    if tmp < target:
                        left += 1
                    else:
                        right -= 1
        return answer

