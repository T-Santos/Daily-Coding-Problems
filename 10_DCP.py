'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''
from threading import Timer 

def scheduler(job,milliseconds):
	seconds = milliseconds/1000
	Timer(seconds,job).start()

def hello_world()
	print("hello_world")

def main():
	scheduler(hello_world,2521)

if __name__ == '__main__':
	main()