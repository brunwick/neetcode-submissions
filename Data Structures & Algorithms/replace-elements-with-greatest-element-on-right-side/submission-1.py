class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        for i in range(l - 1):
            right_max = max(arr[i+1:])
            arr[i] = right_max
        arr[-1] = -1
        return arr