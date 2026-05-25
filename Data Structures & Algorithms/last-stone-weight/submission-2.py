class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone2 > stone1:
                heapq.heappush(stones, stone1 - stone2)

        if stones != []:
            return stones[0] * -1
        
        return 0