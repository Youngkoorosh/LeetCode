# Last updated: 7/3/2025, 6:04:00 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        res=[1]*n

        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        return res        

        
        """
        n=len(nums)
        res=[1]*n

        for i in range(n):
            prod=1
            for j in range(n):
                if i!=j:
                    prod *= nums[j]
            res.append(prod)
        return res        
"""

            
            
        