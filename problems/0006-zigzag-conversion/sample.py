class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1: return s

        l = 0
        p = 1
        arr = [""] * numRows
        output = ""
        
        for i in range (len(s)):
            arr[l] += s[i]
            l += p
            if l == 0 or l == numRows -1:
                p *= -1
        
        for j in range (numRows):
            output += arr[j]

        return output
