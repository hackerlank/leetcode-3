import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # cache dict constructed by value and used count
        self.cache = collections.defaultdict(lambda : [-1, 0])
        self.capacity = capacity

    def __str__(self):
        return 'LRU: {0}'.format(self.cache.items())

    def get_least_used_key(self, lst):
        return min(lst, key=lambda x: x[1])[0]

    # @return an integer
    def get(self, key):
        self.cache[key][1] += 1
        return self.cache[key][0]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            lst = [(key, count) for key, (_, count) in self.cache.items()]
            least_used_key = self.get_least_used_key(lst)
            del self.cache[least_used_key]
        self.cache[key][0] = value

if __name__ == '__main__':
    lru = LRUCache(3)
    lru.set('a', 10)
    lru.set('b', 20)
    lru.set('c', 30)
    print lru.get('b')
    print lru.get('c')
    print lru
    lru.set('d', 40)
    print lru.get('d')
    print lru
