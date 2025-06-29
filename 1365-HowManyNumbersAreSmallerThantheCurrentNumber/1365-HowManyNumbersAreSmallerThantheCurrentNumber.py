# Last updated: 6/29/2025, 7:05:40 AM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        how_many = []
        counter=0
        for i in nums:
            for j in nums:
                if i>j :
                    counter+=1
            how_many.append(counter)
            counter=0
        return how_many
