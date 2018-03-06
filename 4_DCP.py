

def find_min_pos_int(array):

	MIN_POS_INT = 1

	if not array:
		return MIN_POS_INT

	min_int = MIN_POS_INT
	next_min_int = 0
	max_int = 0

	for next_int in array:

		if next_int < MIN_POS_INT:
			continue

		if not next_min_int:
			next_min_int = next_int

		if not max_int:
			next_min_int = next_int

		if next_int < min_int:
			next_min_int = min_int
			min_int = next_int

		if next_int > max_int:
			max_int = next_int

	# return more more than the last amount found
	if (next_min_int - min_int) == 2:
		return min_int+1
	else:
		return max_int+1

def unit_tests():

	# known examples
	assert find_min_pos_int([3,4,-1,1]) == 2, "[3,4,-1,1] is not 2"
	assert find_min_pos_int([1,2,0]) == 3, "[1,2,0] is not 3"

	# additional tests
	assert find_min_pos_int([]) == 1, "[] is not 1"
	assert find_min_pos_int([-1,0]) == 1, "[-1,0] is not 1"
	assert find_min_pos_int([-1,-1,-1]) == 1, "[-1,0] is not 1"

	assert find_min_pos_int([2,3,1,3,1,2,0]) == 4, "[2,3,1,3,1,2,0] is not 4"
	assert find_min_pos_int([2,3,4,3,1,2,0]) == 5, "[2,3,4,3,1,2,0] is not 5"
	print("Test Success")
	return 1

def main():
	unit_tests()

if __name__ == '__main__':
	main()