class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            minHeap.append([points[i][0] ** 2 + points[i][1] ** 2, points[i][0], points[i][1]])

        heapq.heapify(minHeap)
        result = []

        for i in range(k):
            i, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result

