# Last updated: 7/2/2025, 4:32:32 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total = ""
        i=0
        j=0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                total += word1[i]
                i += 1
            if j < len(word2):
                total += word2[j]
                j += 1
        return total
