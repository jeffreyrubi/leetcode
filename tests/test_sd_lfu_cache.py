from src.sd_lfu_cache import LFUCache


def test_sd_lfu_cache():
    # Test case 1: Basic operations with capacity 2
    cache = LFUCache(2)
    
    # Test putting and getting values
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # returns 1
    
    # At this point, key 1 has frequency 2, key 2 has frequency 1
    cache.put(3, 3)  # key 2 evicted (LFU), cache is now {1=1, 3=3}
    assert cache.get(2) == -1  # returns -1 (not found)
    assert cache.get(3) == 3   # returns 3
    
    cache.put(4, 4)  # key 3 evicted (LFU), cache is now {1=1, 4=4}
    assert cache.get(1) == -1   # returns 1
    assert cache.get(3) == 3  # returns -1 (not found)
    assert cache.get(4) == 4   # returns 4
    


def test_sd_lfu_cache_update_existing():
    # Test case 2: Updating existing keys
    cache = LFUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # Update existing key, should not evict anything
    assert cache.get(1) == 10
    assert cache.get(2) == 2


def test_sd_lfu_cache_capacity_one():
    # Test case 3: Cache with capacity 1
    cache = LFUCache(1)
    
    cache.put(1, 1)
    assert cache.get(1) == 1
    
    cache.put(2, 2)  # Should evict key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_sd_lfu_cache_frequency_tie():
    # Test case 4: When frequencies are tied, evict the least recently used
    cache = LFUCache(2)
    
    cache.put(1, 1)  # freq: {1: 1}
    cache.put(2, 2)  # freq: {1: 1, 2: 1}
    
    # Both have same frequency, so when we add a third item, 
    # the least recently used (key 1) should be evicted
    cache.put(3, 3)
    assert cache.get(1) == -1  # key 1 should be evicted
    assert cache.get(2) == 2
    assert cache.get(3) == 3


def test_sd_lfu_cache_complex_scenario():
    # Test case 5: More complex scenario
    cache = LFUCache(3)
    
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)  # Should evict one of 1,2,3 (least frequent + least recent)
    
    # Access patterns to create different frequencies
    cache.get(4)  # 4: freq 2
    cache.get(4)  # 4: freq 3
    cache.get(2)  # 2: freq 2
    cache.get(2)  # 2: freq 3
    cache.get(2)  # 2: freq 4
    
    # Now add another item - should evict the one with lowest frequency
    cache.put(5, 5)
    
    # The keys with highest frequency should still be there
    assert cache.get(2) > 0  # Should still exist
    assert cache.get(4) > 0  # Should still exist


def test_sd_lfu_cache_empty():
    # Test case 6: Getting from empty cache
    cache = LFUCache(1)
    assert cache.get(1) == -1