import copy

class Node:
	def __init__(self, value = None, right = None, left = None):
		self.value = value 
		self.right = right 
		self.left = left  

def get_short_path(root, a, b):
	lca = find_lca(root, a, b).get("lca")
	result = []
	final_result = []
	if lca.value  > a.value:
		left = a
		right = b
	else: 
		left = b 
		right = a  

	#helper(lca, left, result, final_result)
	path = []
	find_path(lca, right, path)
	path.append(lca)
	path.reverse()
	s = "->".join(["node %d" % n.value for n in path])
	# for node in path:
		# sub_s = " value: {}".format(node.value)
		# s += sub_s 
	print(s)
	# right_path = helper(lca, right, result)
	# return left_path.reverse() + right_path[1:]

def find_path(start, target, path):
	if not start:
		return False
	if start.value == target.value:
		return True
	if find_path(start.left, target, path):
		path.append(start.left)
		return True
	if find_path(start.right, target, path):
		path.append(start.right)
		return True
	return False


# def helper(start, target, path, final_result):
# 	if not start:
# 		return 

# 	path.append(start)	 
# 	if path[-1] == target:
# 		final_result = copy.deepcopy(path)
# 		return 
	
# 	helper(start.left, target, path, final_result)
# 	path.pop()
# 	helper(start.right, target, path, final_result)	
# 	return 
		
def find_lca(root, a, b):

	if not root:
		return {"lca": False, "a": False, "b": False} 

	left = find_lca(root.left, a, b)
	right = find_lca(root.right, a, b)
	
	if left.get("lca"): 
		return left
	elif right.get("lca"):
		return right
	elif root == a and (left.get("b") or right.get("b")):
		return {"lca": root, "a": True, "b": True}
	elif root == a:
		return {"lca": False, "a": True, "b": False}
	elif root == b and (left.get("a") or right.get("a")):
		return {"lca": root, "a": True, "b": True}
	elif root == b:
		return {"lca": False, "a": False, "b": True}
	elif left.get("a") and right.get("b") or left.get("b") and right.get("a"):
		return {"lca": root, "a": True, "b": True}
	else:
		return {"lca": False, "a": left.get("a") or right.get("a"), "b": left.get("b") or right.get("b")}


# 0
# |  |
# 1   2 
# | |  |  | 
# 3  4  5  6 
# || || || || 
# 78 910 1112  1314

n0 = Node(0, None, None)
n1 = Node(1, None, None)
n2 = Node(2, None, None)
n0.left = n1
n0.right = n2 
n3 = Node(3, None, None)
n4 = Node(4, None, None)
n1.left = n3
n1.right = n4
n5 = Node(5, None, None)
n6 = Node(6, None, None)
n2.left = n5
n2.right = n6

# result = find_lca(n0, n6, n1)
# print(result.get("lca").value)

print(get_short_path(n0, n6, n1))