import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        left = 1
        right = max(piles)
        min_k = right

        while left <= right:
            mid = left + ((right - left) // 2)
            hours = 0
         
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)

            if hours <= h:
                if mid < min_k:
                    min_k = mid

                right = mid - 1
            
            else:
                left = mid + 1

        return min_k