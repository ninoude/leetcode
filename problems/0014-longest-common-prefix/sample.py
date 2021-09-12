from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(min(strs, key=len)) == 0: return ""
        prefix = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

