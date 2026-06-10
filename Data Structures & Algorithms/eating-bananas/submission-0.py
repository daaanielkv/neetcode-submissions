class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += pile // mid if pile % mid == 0 else pile // mid + 1
            if total > h:
                l = mid + 1
            else:
                r = mid
                
        return l