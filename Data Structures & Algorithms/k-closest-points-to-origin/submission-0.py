class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDist(point: List[int]) -> float:
            return math.sqrt(point[0]**2 + point[1]**2)

        def quickSort(arr: List[int], s: int, e: int) -> None:
            if e - s + 1 <= 1:
                return arr

            pivot = getDist(arr[e])
            left  = s

            for i in range(s, e):
                if getDist(arr[i]) < pivot:
                    arr[i], arr[left] = arr[left], arr[i]
                    left += 1

            arr[left], arr[e] = arr[e], arr[left]

            quickSort(arr, s, left - 1)
            quickSort(arr, left + 1, e)

        quickSort(points, 0, len(points) - 1)
        return points[0:k]