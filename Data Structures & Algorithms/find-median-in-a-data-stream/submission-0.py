class MedianFinder:
    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        """Adds a number to the stream"""
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1 * num)

        # Balanceamento
        self.balance_heap()
        
    def balance_heap(self) -> None:
        """
        Keeps both halfs of the array balanced.
        Lenght difference must be at most 1 due to odd-length streams.
        """
        if len(self.left) > len(self.right) + 1:
            # Lado esquerdo maior
            temp = heapq.heappop(self.left)
            heapq.heappush(self.right, -1 * temp)
        elif len(self.right) > len(self.left) + 1:
            # Lado esquerdo maior
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * temp)
    
    def findMedian(self) -> int:
        """Finds the median of the stream"""
        # Se for ímpar, a mediana é o valor do meio do array.
        # Se for par, a mediana é a média dos dois valores do meio do array.
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (-1 * self.left[0] + self.right[0]) / 2
        
        