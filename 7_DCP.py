'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.
'''

NUMBER_LETTER_MAP = {str(number): chr(96+number) for number in range(1,27)}


def number_of_decodings(message):

	if not message:
		return 0

	if '0' in message:
		return 0

	def number_of_decodings_helper(current_decode,message):

		if not message:
			if current_decode not in unique_decode_dict:
				unique_decode_dict[current_decode] = None
			return
		else:
			# check next number
			new_current_decode = current_decode + NUMBER_LETTER_MAP[message[0]]
			number_of_decodings_helper(
				new_current_decode,
				message[1:])
			# check next two numbers
			if (len(message)>1
				and ((message[0]+message[1]) in NUMBER_LETTER_MAP)):
				new_current_decode = current_decode + NUMBER_LETTER_MAP[(message[0]+message[1])]
				number_of_decodings_helper(
					new_current_decode,
					message[2:])

	unique_decode_dict = {}
	number_of_decodings_helper('',message)
	return len(unique_decode_dict)

def unit_tests():
	
	assert number_of_decodings('') == 0, "'' is not 0"
	assert number_of_decodings('0') == 0, "0 is not 0"
	assert number_of_decodings('111') == 3, "111 is not 3"
	assert number_of_decodings('999') == 1, "999 is not 1"
	assert number_of_decodings('7743681176') == 3, "7743681197 is not 3"
	print('PASS')

def main():
	unit_tests()

if __name__ == '__main__':
	main()