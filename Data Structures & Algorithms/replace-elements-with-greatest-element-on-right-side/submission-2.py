class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        l = len(arr)
        for i in range(l - 1):
            if arr[i +1] < right_max:
                arr[i] = right_max
            else:
                arr[i] = max(arr[i +1:])
        arr[-1] = -1
        return arr