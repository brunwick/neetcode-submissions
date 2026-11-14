class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur, best = 0, 0
        for n in nums:
            cur = cur + 1 if n == 1 else 0
            best = max(best, cur)
        return best