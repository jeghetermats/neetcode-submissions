class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
    def get(self, key: int) -> int:
        if not key in self.cache: return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return self.cache.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if len(self.cache)< self.capacity or key in self.cache:
            if key in self.cache:
                del self.cache[key]
            self.cache[key] = value
        else:
            if key in self.cache:
                del self.cache[key]
            self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value