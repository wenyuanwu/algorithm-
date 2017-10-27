class Node:
	def __init__(self, value = None, right = None, left = None, parent = None):
		self.value = value 
		self.right = right 
		self.left = left 
		self.parent = parent 


def get_short_path(root, a, b):
	height_a, height_b = get_height(root, a), get_height(root, b)

	if height_a > height_b:
		first_half_result = traverse_to_same_height(a, b, height_a, height_b)
		second_half_result = [b]		
	else:
		first_half_result = traverse_to_same_height(b, a, height_b, height_a)
		second_half_result = [a]

	while first_half_result[-1] != second_half_result[0]:
		first_half_parent = first_half_result[-1].parent 
		first_half_result.append(first_half_parent)
		second_half_parent = second_half_result[0].parent
		second_half_result.insert(0, second_half_parent)	

	first_half_result.extend(second_half_result[1:])
	return first_half_result	

def get_height(root, node):
	height = 0 
	while node != root:
		height += 1
		node = node.parent 
	return height 

def traverse_to_same_height(larger_height_node, smaller_height_node, larger_height, smaller_height):
	result = []
	result.append(larger_height_node)
	while larger_height != smaller_height:
		parent_node = result[-1].parent
		result.append(parent_node)
		larger_height -= 1
	return result 	


# 0
# |  |
# 1   2 
# | |  |  | 
# 3  4  5  6 
# || || || || 
# 78 910 1112  1314



n0 = Node(0, None, None, None)
n1 = Node(1, None, None, n0)
n2 = Node(2, None, None, n0)
n0.left = n1
n0.right = n2 
n3 = Node(3, None, None, n1)
n4 = Node(4, None, None, n1)
n1.left = n3
n1.right = n4
n5 = Node(5, None, None, n2)
n6 = Node(6, None, None, n2)
n2.left = n5
n2.right = n6

# print(n0.value)
# print(n0.left.left.value)
# print(n0.right.left.value) 

arr = get_short_path(n0,n1,n5)
for el in arr:
	print("value: {} ".format(el.value))

