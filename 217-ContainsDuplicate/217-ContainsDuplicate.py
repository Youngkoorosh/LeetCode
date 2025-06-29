# Last updated: 6/29/2025, 5:24:25 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        unique = list(set(nums))
        unique.sort()
        if unique == nums:
            return False
        else:
            return True