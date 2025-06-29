# Last updated: 6/29/2025, 5:24:27 AM
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  
                if nums[i] + nums[j] == target:
                    return [i, j]



        