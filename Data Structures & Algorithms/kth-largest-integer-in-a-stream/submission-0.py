class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        # now we only want to keep the k largest values in the heap
        while self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # adding val to the stream
        heapq.heappush(self.minHeap, val)
        # we need to account for the added value and pop the smallest
        # value if and only if the heap length is greater than k

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # now the kth largest integer is the smallest value of the min heap
        return self.minHeap[0]


        
