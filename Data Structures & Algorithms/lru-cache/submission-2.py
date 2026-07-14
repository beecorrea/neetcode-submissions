class LRUCache:

    def __init__(self, capacity: int):
        # Initialize capacity constraint.
        self.capacity = capacity
        # We use an ordered hash map to do O(1) lookups.
        # It also allows O(1) eviction.
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update frequency and overwrite value.
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # Cache is full, evict least recently used.
                # When last=False, popitem() uses FIFO for popping.
                lru = self.cache.popitem(last=False)
            # Add new kv
            self.cache[key] = value

        
