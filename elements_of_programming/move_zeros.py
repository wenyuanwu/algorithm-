def moveZeros(nums):
	if not nums:
		return []

	count = 0
	last_idx = 0 
	for i in range(len(nums)):		
		if nums[i] == 0:
			count += 1
			continue
		nums[i - count] = nums[i]
		last_idx = i - count 

	for i in range(last_idx + 1, len(nums)):
		nums[i] = 0 

	return nums 

a = [0,0,0,1,0,3,0,0,12,0,8,100]
print(moveZeros(a))

b = None
print(moveZeros(b))
