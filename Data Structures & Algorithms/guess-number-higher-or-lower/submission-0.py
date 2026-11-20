# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo <= hi:
            mid = (hi + lo) // 2

            response = guess(mid)
            if response < 0: # num is lower than pick
                hi = mid - 1
            elif response > 0: # num is higher than pick
                lo = mid + 1
            else:
                return mid