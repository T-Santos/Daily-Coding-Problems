'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)
Implement car and cdr.
'''


def car(f):
	#return f(lambda p,q: (p,q))[0]
	return f(lambda p,q: p)

def cdr(f):
	#return f(lambda p,q: (p,q))[1]
	return f(lambda p,q: q)

def cons(a,b):
	return lambda f : f(a,b)

def unit_tests():
	assert car(cons(3,4))==3, "car(cons(3,4)) is not 3"
	assert cdr(cons(3,4))==4, "cdr(cons(3,4)) is not 4"

	print("Test Successful")
	return 1

def main():

	unit_tests()

if __name__ == '__main__':
	main()