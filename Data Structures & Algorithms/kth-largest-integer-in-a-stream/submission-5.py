class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) == 0:
            self.heap = [] 
        else: 
            self.heap = [num for num in nums]
        
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]        
