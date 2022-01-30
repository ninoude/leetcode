class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        x = abs(dividend)
        y = abs(divisor)
        origin = y

        i = 0
        j = 1

        while x >= origin:
            x -= y
            i += j
            if x >= (y << 1):
                y <<= 1
                j <<= 1
            else:
                y = origin
                j = 1

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            i = -i
        return min(2**31-1, max(-2**31, i))
