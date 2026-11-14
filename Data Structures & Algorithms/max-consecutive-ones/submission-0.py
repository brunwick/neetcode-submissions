class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        consec = 0
        for n in nums:
            if n == 1:
                consec += 1
            else:
                res.append(consec)
                consec = 0
        res.append(consec)
        return max(res)