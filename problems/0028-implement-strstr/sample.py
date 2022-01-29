class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len > h_len: return -1
        if n_len == 0: return 0

        for i in range(h_len-n_len+1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1

