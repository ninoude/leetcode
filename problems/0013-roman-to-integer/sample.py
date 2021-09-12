class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = { "M": 1000, "D": 500, "C": 100, "L": 50,
                      "X": 10,   "V": 5,   "I": 1}
        answer = 0
        prev = ""
        for c in s:
            answer += roman_num[c]
            if (c == 'V' or c == 'X') and prev == 'I': answer -= 2
            if (c == 'L' or c == 'C') and prev == 'X': answer -= 20
            if (c == 'D' or c == 'M') and prev == 'C': answer -= 200
            prev = c

        return answer

