import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) < 1: return 0

        flag_minus = 0
        output = 0
        if s[0] == '-':
            flag_minus = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        output_str = ""
        output_str = re.findall('[0-9]*', s)[0]

        if output_str == "": return 0
        
        if flag_minus == 1:
            output = int(output_str)
            output *= -1
        else:
            output = int(output_str)

        if output < -2147483648: return -2147483648
        if 2147483647 < output: return 2147483647

        return output
