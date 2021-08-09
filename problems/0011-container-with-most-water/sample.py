from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_y = height[0]
        i = 0
        j = len(height)-1
        tmp = 0
        w = 0

        while i < len(height):
            if max_y < height[i]: max_y = height[i]
            if max_y > height[i]:
                i+=1
                continue
            while j > i: 
                if height[i] < height[j]:
                    tmp = height[i] * (j-i)
                    if w < tmp: w = tmp
                    break
                else:
                    tmp = height[j] * (j-i)
                if w < tmp: w = tmp
                j-=1
            i+=1
            j=len(height)-1
        return w

