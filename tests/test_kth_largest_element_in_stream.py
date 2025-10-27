from src.kth_largest_element_in_stream import KthLargest

def test_kth_largest_element_in_stream():
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    # Test case 1: Basic usage
    obj = KthLargest(3, [4,5,8,2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

    # Test case 2: k equals desired rank within stream
    obj = KthLargest(3, [2,3])
    assert obj.add(1) == 1
    assert obj.add(5) == 2

    # Test case 3: consecutive adds
    obj = KthLargest(1, [])
    assert obj.add(-1) == -1
    assert obj.add(1) == 1

