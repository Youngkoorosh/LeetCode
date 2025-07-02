# Last updated: 7/2/2025, 5:04:47 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        cleanedStr = " ".join(s.split())
        cleanedStr = cleanedStr.strip()
        parts = cleanedStr.split(" ")
        reversed_parts = parts[::-1] 
        result = " ".join(reversed_parts)
        return result
 