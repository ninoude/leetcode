class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        dic = {")":"(", "}":"{", "]":"["}
        for char in s:
            if arr != [] and char in dic and arr[-1] == dic[char]:
                arr.pop(-1)
            else:
                arr.append(char)
        return arr == []
