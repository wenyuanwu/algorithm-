import random

def my_shuffle(list):
	if not list:
		return []
	if len(list) == 1:
		return list

	for i in range(len(list) - 1):

		start_idx = i
		dest_idx = get_random(start_idx, len(list) - 1)
		if start_idx != dest_idx:
			list[start_idx], list[dest_idx] = list[dest_idx], list[start_idx]

	return list

def get_random(floor, ceiling):	
	return random.randint(floor, ceiling)

a = [1,2,3]
print(my_shuffle(a))