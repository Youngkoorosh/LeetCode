class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0  # اندیسی که عددهای غیرصفر رو اونجا قرار می‌دیم

        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        while pos < len(nums):
            nums[pos] = 0
            pos+=1
        
        return nums