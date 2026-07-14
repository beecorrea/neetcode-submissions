class LRUCache:

    def __init__(self, capacity: int):
        # We use a hash map to do O(1) lookups.
        self.cache = dict()
        # We use a doubly linked list to keep the frequency list.
        self.freq = collections.deque()
        # Initialize capacity constraint.
        self.capacity = capacity

    def to_front(self, key: int) -> None:
        self.freq.remove(key)
        self.freq.appendleft(key)

    def get(self, key: int) -> int:
        # Whenever we retrieve a value, we add it
        # to the head of the list.
        if key in self.cache:
            self.to_front(key)

        return self.cache.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.to_front(key)
        else:
            if len(self.cache) >= self.capacity:
                # Cache is full, evict least recently used.
                lru = self.freq.pop()
                del self.cache[lru]
            # Add new kv
            self.cache[key] = value
            self.freq.appendleft(key)

        
