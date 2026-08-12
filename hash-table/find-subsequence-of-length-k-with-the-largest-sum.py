class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(nums, reverse=True)[:k]

        result = []
        for num in nums:
            if num in top_k:
                result.append(num)
                top_k.remove(num)  # اطمینان از اینکه هر عدد فقط یک بار اضافه بشه
        return result
        return result
        