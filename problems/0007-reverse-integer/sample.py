class Solution:
    def reverse(self, x: int) -> int:
        x_str = ""
        flag_minus = 0
        output = 0
        if x < 0:
            x *=-1
            flag_minus = 1
            
        x_str = str(x)
        output_str = x_str[::-1]

        if flag_minus == 1:
            output = int(output_str)
            output *= -1
        else:
            output = int(output_str)

#        if output < -2**31 or 2**31-1 < output:
        if output < -2147483648 or 2147483647 < output:
            return 0
        return output
