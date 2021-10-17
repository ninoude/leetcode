class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if (char == ')' or char == '}' or char == ']'):
                if arr == []: return False
                if (char == ')' and arr[-1] != '('): return False
                if (char == '}' and arr[-1] != '{'): return False
                if (char == ']' and arr[-1] != '['): return False
                arr.pop(-1)
            else:
                arr.append(char)
        return arr == []
