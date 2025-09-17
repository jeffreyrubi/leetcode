from src.min_stack import MinStack

def test_min_stack():

	# Test case 1: Basic push/pop/getMin
	stack = MinStack()
	stack.push(-2)
	stack.push(0)
	stack.push(-3)
	assert stack.getMin() == -3
	stack.pop()
	assert stack.top() == 0
	assert stack.getMin() == -2

	# Test case 2: Push increasing values
	stack = MinStack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	assert stack.getMin() == 1
	stack.pop()
	stack.pop()
	assert stack.getMin() == 1

	# Test case 3: Push decreasing values
	stack = MinStack()
	stack.push(3)
	stack.push(2)
	stack.push(1)
	assert stack.getMin() == 1
	
	# Test case 4: Command sequence
	stack = MinStack()
	stack.push(0)
	stack.push(1)
	stack.push(0)
	assert stack.getMin() == 0
	stack.pop()
	assert stack.getMin() == 0
	stack.pop()
	assert stack.getMin() == 0
	stack.pop()
	stack.push(-2)
	stack.push(-1)
	stack.push(-2)
	assert stack.getMin() == -2
	stack.pop()
	assert stack.top() == -1
	assert stack.getMin() == -2
	stack.pop()
	assert stack.getMin() == -2
	stack.pop()