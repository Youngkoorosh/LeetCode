# Last updated: 7/2/2025, 3:52:20 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1

        if n <= count:
            return True
        else:
            return False
        