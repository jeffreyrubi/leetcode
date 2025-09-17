from src.lru_cache import LRUCache

def test_lru_cache():
	# Test case 1: Basic put/get
	cache = LRUCache(2)
	cache.put(1, 1)
	cache.put(2, 2)
	assert cache.get(1) == 1

	# Test case 2: Eviction
	cache.put(3, 3)  # evicts key 2
	assert cache.get(2) == -1
	cache.put(4, 4)  # evicts key 1
	assert cache.get(1) == -1
	assert cache.get(3) == 3
	assert cache.get(4) == 4

	# Test case 3: Update value
	cache = LRUCache(2)
	cache.put(1, 1)
	cache.put(2, 2)
	cache.put(1, 10)  # update value for key 1
	assert cache.get(1) == 10


    # Test case 4:
	cache = LRUCache(2)
	cache.put(2,1)
	cache.put(1,1)
	cache.put(2,3)
	cache.put(4,1)
	assert cache.get(1) == -1
	assert cache.get(2) == 3
	