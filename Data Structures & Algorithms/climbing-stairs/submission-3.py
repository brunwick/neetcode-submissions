class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        for i in range(int(n // 2) + 1):
            res += int(math.factorial(n - i) / (math.factorial(i) * math.factorial(n - 2 * i)))
        return res
