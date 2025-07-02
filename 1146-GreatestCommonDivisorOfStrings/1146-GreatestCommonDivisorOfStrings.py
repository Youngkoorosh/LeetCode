# Last updated: 7/2/2025, 4:32:34 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ic = ""
        # Check if concatenations are equal in both orders
        if str1 + str2 == str2 + str1:
            # Find the GCD of lengths
            max_len = gcd(len(str1), len(str2))
            ic = str1[:max_len]
                
        return ic
        