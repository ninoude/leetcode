from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1
        arr.extend(nums2)
        arr = sorted(arr)

        if len(arr) % 2 == 1:
            return float(arr[int(len(arr)/2)])
        else:
            return float((arr[int(len(arr)/2)] + arr[int(len(arr)/2-1)]) / 2 )
        return 0
