'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def get_products(list_of_nums):

	list_length = len(list_of_nums)
	list_of_products = [None] * list_length

	left_products = [None] * list_length
	right_products = [None] * list_length

	# get all the items (mult 1 before cur positon)
	# going left to right
	cur_temp_prod = 1
	for offset in range(list_length):
		left_products[offset] = cur_temp_prod
		cur_temp_prod = cur_temp_prod * list_of_nums[offset]

	# get all the items (mult 1 after cur pos)
	# going right to left
	cur_temp_prod = 1
	for pos in range(list_length):
		offset = list_length-pos-1
		right_products[offset] = cur_temp_prod
		cur_temp_prod = cur_temp_prod * list_of_nums[offset]

	for offset in range(list_length):
		list_of_products[offset] = left_products[offset] * right_products[offset]

	return list_of_products
	

def main():

	_input = [1,2,3,4,5]
	#_input = [3,2,1]

	print(_input)
	products = get_products(_input)
	print(products)


if __name__ == '__main__':
	main()