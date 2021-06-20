class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = ""
        x_str = str(x)
        x_str = x_str[::-1]

        if x == int(x_str):
            return True
        else:
            return False

        return 0
