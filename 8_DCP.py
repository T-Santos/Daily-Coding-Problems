'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes have the same value.

Given the root to a binary tree, count the number of unival subtrees.
'''

from collections import deque

class BinaryTree(object):
	"""docstring for ClassName"""
	def __init__(self,):
		self.root = None

	def __str__(self):

		next_nodes = deque([self.root])

		out_nodes = []

		while next_nodes:

			current_node = next_nodes.popleft()

			out_nodes.append(current_node.value)

			if current_node.left_pointer:
				next_nodes.append(current_node.left_pointer)
			if current_node.right_pointer:
				next_nodes.append(current_node.right_pointer) 

		return str(out_nodes)


	def add_node(self,node):

		if not self.root:
			self.root = node
		else:

			next_nodes = deque([self.root])

			while next_nodes:

				current_node = next_nodes.popleft()

				if (not current_node.left_pointer
					or not current_node.right_pointer):
					break
				else:
					next_nodes.append(current_node.left_pointer)
					next_nodes.append(current_node.right_pointer)

			if not current_node.left_pointer:
				current_node.left_pointer = node
			else:
				current_node.right_pointer = node

	def count_unival_subtrees(self):

		if not self.root:
			return 0

		if (not self.root.left_pointer
			and not self.root.right_pointer):
			return 1

		unival_count = 0

		def count_helper(root):

			nonlocal unival_count

			if (not root.left_pointer
				and not root.right_pointer):
				unival_count += 1
				return True
			else:

				l_result = True
				r_result = True
				l_child_is_same = False
				r_child_is_same = False

				if root.left_pointer:
					l_child_is_same = root.left_pointer.value == root.value
					l_result = count_helper(root.left_pointer)

				if root.right_pointer:
					r_child_is_same = root.right_pointer.value == root.value
					r_result = count_helper(root.right_pointer)

				if l_result and r_result and r_child_is_same and l_child_is_same:
					unival_count += 1
					return True
				else:
					return False

		count_helper(self.root)

		return unival_count


class Node(object):

	counter = 0

	def __init__(self,value):
		self.value = value
		type(self).counter += 1
		self.id = type(self).counter
		self.left_pointer = None
		self.right_pointer = None

	def __str__(self):
		return '{}-{}'.format(self.value,self.id)


def case_1():

	tree = BinaryTree()

	n1 = Node('a')
	n2 = Node('a')
	n3 = Node('a')
	n4 = Node('a')
	n5 = Node('a')
	n6 = Node('A')

	n1.left_pointer = n2
	n1.right_pointer = n3

	n3.left_pointer = n4
	n3.right_pointer = n5

	n5.right_pointer = n6

	tree.add_node(n1)

	return tree

def case_2():

	tree = BinaryTree()

	n1 = Node('a')
	n2 = Node('a')
	n3 = Node('a')
	n4 = Node('a')
	n5 = Node('a')
	n6 = Node('A')

	tree.add_node(n1)
	tree.add_node(n2)
	tree.add_node(n3)
	tree.add_node(n4)
	tree.add_node(n5)
	tree.add_node(n6)

	return tree


def unit_tests():

	assert case_1().count_unival_subtrees() == 3
	assert case_2().count_unival_subtrees() == 4
	print("PASS")

def main():

	unit_tests()

if __name__ == '__main__':
	main()