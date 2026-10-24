class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        rev *= sign
        if rev < MIN or rev > MAX:
            return 0
        return rev
        