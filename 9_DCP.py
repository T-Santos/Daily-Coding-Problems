'''
Given a list of integers, write a function that returns the
largest sum of non-adjacent numbers.

For example:
[2, 4, 6, 8] should return 12, since we pick 4 and 8. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''
#from math import abs

def largest_sum_1(numbers):
	# O(N^2) solution - nested loops

	if not numbers:
		return 0

	if len(numbers) <= 2:
		return 0

	largest = 0

	for num_1_pos, num_1 in enumerate(numbers[:-2]):

		for num_2 in numbers[num_1_pos+2:]:

			largest = num_1 + num_2 if num_1 + num_2 > largest else largest

	return largest

def largest_sum(numbers):
	# O(nlogn) - for the sort

	if not numbers:
		return 0
	if len(numbers) <= 2:
		return 0

	sort_pos = sorted(
		[(number,position) for position,number in enumerate(numbers)],
		reverse = True,
		key = lambda x: x[0])

	largest = sort_pos[0]
	second_largest = sort_pos[1] if abs(sort_pos[0][1] - sort_pos[1][1]) > 1 else sort_pos[2]

	return largest[0] + second_largest[0]

def unit_tests():

	assert largest_sum([]) == 0
	assert largest_sum([1,2]) == 0
	assert largest_sum([1,1,1]) == 2
	assert largest_sum([1,2,3]) == 4
	assert largest_sum([2,4,6,8]) == 12
	assert largest_sum([5,1,1,5]) == 10
	assert largest_sum([2,8,3,8]) == 16
	assert largest_sum([5,4,3,2,1]) == 8
	print("PASS")

def main():
	unit_tests()

if __name__ == '__main__':
	main()