from collections import deque

class LRU_Cache(object):
    '''
    Cache uses a dictionary as a cache and a queue to monitor the oldest key.
    self.cache - dictionary of the cache O(1) for get().
    self.queue - queue for monitoring the oldest used key.
    '''
    def __init__(self, capacity = 5):
        if capacity <= 0:
            raise ValueError('LRU Cache Capacity must be more than 0.')
        self.capacity = capacity
        self.cache = dict()
        self.current_load = 0
        self.queue = deque()

    def get(self, key):
        if key in self.cache:
            output_value = self.cache[key]
            self.queue.remove(key)
            self.queue.appendleft(key)
            return output_value
        else:
            return -1

    def set(self, key, value):
        if key not in self.cache:
            if self.current_load == self.capacity:
                self._removeOldestKey()
            self.cache[key] = value
            self.current_load += 1
            self.queue.appendleft(key)

    def _removeOldestKey(self):
        deleting_key = self.queue.pop()
        del self.cache[deleting_key]
        self.current_load -= 1


    def __repr__(self):
        return f'{self.queue}'


def test1():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);


    assert our_cache.get(1) == 1, 'Test 1 failed' # returns 1
    assert our_cache.get(2) == 2, ' Test 2 failed'  # returns 2
    assert our_cache.get(9) == -1, 'Test 3 failed' # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1, 'Test 4 failed'

def test2():
    try:
        our_cache0 = LRU_Cache(0)

        # Check if our_cache variable fails to be created (capacity cannot be = 0).
        # Hence,it should not be in local namespace/variable.
        assert 'our_cache0' in locals(), 'test2 should raise a ValueError for cache capacity of 0!'
    except ValueError:
        # Check if valueError was raised for capacity == 0.
        print('ValueError was successful/correctly raised for test2, capacity == 0, edged case')


def test3():
    try:
        our_cacheNegative = LRU_Cache(-1)
        # Check if our_cache variable fails to be created (capacity cannot be < 0).
        # Hence,it should not be in local namespace/variable.
        print(locals())
        assert 'our_cacheNegative' in locals(), 'test3 should raise a ValueError for cache capacity of 0!'
    except ValueError:
        # Check if valueError was raised for capcity == 0.
        print('ValueError was successful/correctly raised for test3, capacity < 0, edge case')



if __name__ == '__main__':
    test1()
    test2()
    test3()
    print('Test done')
