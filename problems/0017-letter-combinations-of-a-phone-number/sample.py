from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = {"1": "",     "2": "abc", "3": "def",
                   "4": "ghi",  "5": "jkl", "6": "mno",
                   "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []

        for n in digits:
            answer = self.product(answer, mapping[n])
        return answer

    def product(self, nums1: List[str], nums2: str):
        answer = []
        if len(nums1) == 0:
            for n in nums2:
                answer.append(n)
            return answer

        for n1 in nums1:
            for n2 in nums2:
                answer.append(n1+n2)
        return answer

