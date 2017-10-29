# 
# Welcome to the Interview!
# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
            
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9

# Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one ancestor.

# Sample input and output:
# [3, 8] => false
# [5, 8] => true
# [6, 8] => true

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 9)
]


def share_ancestor(idx1, idx2, pairs):
	relation_map = translate_to_map(pairs)
	idx1_parent_path = find_parent_path(idx1, relation_map)
	idx2_parent_path = find_parent_path(idx2, relation_map)

	for parent in idx1_parent_path:
		if parent in idx2_parent_path:
			return True
	return False 

def find_parent_path(idx, relation_map):
	result = []
	q = relation_map[idx]
	while q:
		current_parent = q.pop()
		result.append(current_parent)
		next_level_parents = relation_map[current_parent]
		if next_level_parents:
			for parent in next_level_parents:
				q.append(parent)

	return result 

def translate_to_map(pairs):
	hm = {}

	for pair in pairs:
		parent = pair[0]
		child = pair[1]
		if hm.get(child):
			hm[child].append(parent)
		else:
			hm[child] = [parent]

		if not hm.get(parent):
			hm[parent] = []

	return hm 

print(share_ancestor(3, 8, pairs))
print(share_ancestor(5, 8, pairs))
print(share_ancestor(6, 8, pairs))
print(share_ancestor(1, 2, pairs))
print(share_ancestor(6, 9, pairs))

