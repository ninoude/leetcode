class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: return False
        
        y = 0
        tmp = x
        while tmp != 0:
            y *=10
            y += tmp % 10
            tmp = int(tmp / 10)

        if x == y:
            return True
        else:
            return False

        return 0
