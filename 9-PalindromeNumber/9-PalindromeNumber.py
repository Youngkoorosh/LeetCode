# Last updated: 6/29/2025, 5:24:26 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
        