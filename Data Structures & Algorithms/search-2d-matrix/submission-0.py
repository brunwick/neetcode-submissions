class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        n = len(matrix[0])

        while lo <= hi:
            mid = (lo + hi) // 2

            if target < matrix[mid][0]:
                hi = mid - 1

            elif target > matrix[mid][n - 1]:
                lo = mid + 1

            else:
                return target in matrix[mid]

        return False
