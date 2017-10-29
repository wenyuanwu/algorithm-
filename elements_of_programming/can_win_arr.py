board = [1, 3, 2, 0, 5, 2, 8, 2]


def can_win(arr):
	visited = {}
	result_map = {}
	result = []
	for i in range(len(arr)):
		if result_map.get(i) is not None:
			result.append((i, result_map[i]))	
		else:
			boolean_value = helper(i, arr, visited, result_map)
			result.append((i, boolean_value))
		print('result_map: %s' % result_map)
	return result 	

# visited = True 
# visited = False 
# visited = "visited"

def helper(idx, arr, visited, result_map):

	if visited.get(idx):
		if result_map.get(idx) is not None:
			return result_map[idx]
		else:
			return False
	else:
		visited[idx] = True
	
	if idx < 0 or idx > len(arr):
		result_map[idx] = False
		return False	

	if arr[idx] == 0:
		result_map[idx] = True
		return True

	delta = arr[idx]

	if helper(idx + delta, arr, visited, result_map) or helper(idx - delta, arr, visited, result_map):
		result_map[idx] = True

	return helper(idx + delta, arr, visited, result_map) or helper(idx - delta, arr, visited, result_map)

print(can_win(board))