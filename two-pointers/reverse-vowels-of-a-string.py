class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        res = ""

        for i in s:
            if i in vowels:
                res+=i
        
        res = ''.join(reversed(res))
        
        j = 0  
        new_s = ""

        for i in s:
            if i in vowels:
                new_s += res[j]
                j += 1
            else:
                new_s += i 

        return new_s

        

