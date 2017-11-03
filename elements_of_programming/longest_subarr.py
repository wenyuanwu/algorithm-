def longest_increasing_sub(arr):
	if not arr:
		return []

	start_idx = 0
	end_idx = 0
	max_len = end_idx - start_idx + 1
	temp_start = 0
	temp_end = 0

	for i in range(1, len(arr)):
		if arr[i] > arr[i-1]:
			temp_end = i 
		else: 
			temp_start = i

		if temp_end - temp_start + 1 > max_len:
			start_idx = temp_start
			end_idx = temp_end
			max_len = end_idx - start_idx + 1

	return arr[start_idx: end_idx + 1]

arr1 = [5,7,1,3,8,9]
arr2 = []
arr3 = [7,6,5]
arr4 = [100,0,3,9,6,-1,10]

print(longest_increasing_sub(arr1))
print(longest_increasing_sub(arr2))
print(longest_increasing_sub(arr3))
print(longest_increasing_sub(arr4))
