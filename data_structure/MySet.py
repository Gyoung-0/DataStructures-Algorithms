class MyHashSet:
    def __init__(self, size=10):
        self.size = size 
        self.buckets = [ [] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size
    
    def add(self, value):
        idx = self._hash(value)
        if value not in self.buckets[idx]:
            self.buckets[idx].append(value)

    def remove(self, value):
        idx = self._hash(value)
        if value in self.buckets[idx]:
            self.buckets[idx].remove(value)

    def __contains__(self, value):
        idx = self._hash(value)
        return value in self.buckets[idx]

    def __str__(self):
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return "{" + ", ".join(map(str, result)) + "}"