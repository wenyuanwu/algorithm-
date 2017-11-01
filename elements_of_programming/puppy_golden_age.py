def puppy_golden_age(years):
	max_sub = years[0]
	start_idx = 0 
	end_idx = 0 

	temp_sum = years[0]
	temp_start_idx = 0
	temp_end_idx = 0

	for idx in range(1, len(years)):
		if temp_sum > 0 and temp_sum + years[idx] > 0:
			temp_sum = temp_sum + years[idx]
			temp_end_idx += 1
		else: 
			temp_sum = years[idx]
			temp_start_idx = idx
			temp_end_idx = idx 
		
		if temp_sum > max_sub:
			max_sub = temp_sum
			start_idx = temp_start_idx
			end_idx = temp_end_idx

	return (start_idx, end_idx)		

ys = [100, -101, 200, -3, 1000]
ys2 = [100, -1, -2, -3, 1,1000]
ys3 = [-2, -3, -1]
# [100, -1, -2, -3, 1,1000]
# [-2, -3, -1]
print(puppy_golden_age(ys))
print(puppy_golden_age(ys2))
print(puppy_golden_age(ys3))