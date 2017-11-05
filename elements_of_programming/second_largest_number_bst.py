class Node:
	def __init__(self, value, left=None, right=None, parent = None):
		self.value = value
		self.left = left
		self.right = right 
		self.parent = parent 

	def add_right_node(self, right):
		self.right = right

	def add_left_node(self, left):
		self.left = left

	def add_parent_node(self, parent):
		self.parent = parent 

	def left(self):
		return self.left

	def right(self):
		return self.right

	def _str(self, node):
		if node.left is None and node.right is None:
			print(node.value)
			return 
		self._str(node.left)
		print(node.value)				
		self._str(node.right)
		return 

def second_largest_bst(root):
	# if root is None or \
	# 	(root.left is None and root.right is None):
	# 		raise Exception("tree must have more than one node")
	if root.left and not root.right:
		return find_largest(root.left)
	if root.right and not root.right.right and not root.right.left:
		return root.value
		
	return second_largest_bst(root.right)
		
def find_largest(root):
	# if root is None or \
	# 	(root.left is None and root.right is None):
	# 		raise Exception("tree must have more than one node")
	if root.right is not None:
		return find_largest(root.right)
	return root.value




n4 = Node(4)
n3 = Node(3)
n9 = Node(9)
n1 = Node(1)
n2 = Node(2)
n6 = Node(6)
n13 = Node(13)
n11 = Node(11)
n5 = Node(5)
n8 = Node(8) 
n4.add_right_node(n9)
n4.add_left_node(n2)
n2.add_right_node(n3)
n2.add_left_node(n1)
n9.add_left_node(n6)
n6.add_left_node(n5)
n6.add_right_node(n8)
# n9.add_right_node(n13)

# n1._str(n4)

print(second_largest_bst(n4))
#    4
#  2   9 
# 1 3 6 
	#5 8