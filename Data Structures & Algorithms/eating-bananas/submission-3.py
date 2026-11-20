class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((p + k - 1) // k for p in piles)
        
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if hours_needed(k) <= h:
                hi = k
            else:
                lo = k + 1
        return lo