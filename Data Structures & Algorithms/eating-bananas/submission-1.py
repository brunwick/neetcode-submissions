class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(k):
            return sum([p // k + 1 if p % k else p / k for p in piles])
        
        lo = 1
        hi = max(piles)
        success = []

        while lo <= hi:
            k = (lo + hi) // 2

            if get_time(k) <= h:
                success.append(k)
                hi = k - 1
            else:
                lo = k + 1
        if success:
            return min(success)
        else:
            return hi