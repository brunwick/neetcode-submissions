# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = pairs[:]
        states = []
        for i in range(len(arr)):
            j = i - 1
            while j >= 0 and arr[j].key > arr[j + 1].key:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
            states.append(arr[:])
        return states