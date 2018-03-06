'''
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwords from the end state.

'''

def interleave_reversed(stack):
	from collections import deque
	queue = deque()

	start = 0 if (len(stack)/2)%2==0 else 1

	for locked_in in range(start,len(stack)):

		# move all into stack up until locked in
		for remove in range(0,(len(stack) - locked_in)):
			queue.append(stack.pop())

		# move them all back into the stack
		for replace in range(0,len(queue)):
			stack.append(queue.popleft())

	return stack

def quick_int(stack):
	from collections import deque
	queue = deque()

	for locked_in in range(1,len(stack)):

		[ queue.append(stack.pop()) for _ in range(len(stack) - locked_in) ]
		[ stack.append(queue.popleft()) for _ in range(len(queue)) ]

	return stack


def interleave(stack):
	from collections import deque
	queue = deque()

	for locked_in in range(1,len(stack)):

		# move all into stack up until locked in
		for remove in range(0,(len(stack) - locked_in)):
			queue.append(stack.pop())

		# move them all back into the stack
		for replace in range(0,len(queue)):
			stack.append(queue.popleft())

	return stack

def interleave_reversed_test():

	assert interleave_reversed([5,4,3,2,1]) == [1,5,2,4,3], "[5,4,3,2,1] is not [1,5,2,4,3]"
	
	assert interleave_reversed([4,3,2,1]) == [1,4,2,3], "[4,3,2,1] is not [1,4,2,3]"

	assert interleave_reversed([1,2,3,'a','b','c']) == [1,'c',2,'b',3,'a'], "[1,2,3,'a','b','c'] is not [1,'c',2,'b',3,'a']"
	print('success')

def interleave_test():

	assert interleave([1,2,3,4,5]) == [1,5,2,4,3], "[1,2,3,4,5] is not [1,5,2,4,3]"
	
	assert interleave([1,2,3,4]) == [1,4,2,3], "[1,2,3,4] is not [1,4,2,3]"

	assert interleave([1,2,3,'a','b','c']) == [1,'c',2,'b',3,'a'], "[1,2,3,'a','b','c'] is not [1,'c',2,'b',3,'a']"

def quick_int_test():

	assert quick_int([1,2,3,4,5]) == [1,5,2,4,3], "[1,2,3,4,5] is not [1,5,2,4,3]"
	
	assert quick_int([1,2,3,4]) == [1,4,2,3], "[1,2,3,4] is not [1,4,2,3]"

	assert quick_int([1,2,3,'a','b','c']) == [1,'c',2,'b',3,'a'], "[1,2,3,'a','b','c'] is not [1,'c',2,'b',3,'a']"
	print('success')

def main():

	quick_int_test()
	interleave_test()
	interleave_reversed_test()

if __name__ == '__main__':
	main()