
count_cache = {}

def find_path(pos1, pos2):
	if (pos1, pos2) not in count_cache.keys():
		x_1, y_1 = pos1
		x_2, y_2 = pos2

		if x_1 > x_2 or y_1 > y_2:
			path = 0  
		elif (x_1 + 1 == x_2) and (y_1 == y_2):
			path = 1
		elif (y_1 + 1 == y_2) and (x_1 == x_2):
			path = 1 
		else: 
			path =  find_path(pos1, (x_2-1, y_2)) + find_path(pos1, (x_2, y_2 -1))	

		count_cache[(pos1, pos2)] = path
	return count_cache[(pos1, pos2)]

print(find_path((0,0), (0,1)))
print(find_path((0,0), (1,1)))
print(find_path((0,0), (2,2)))
print(find_path((0,0), (3,4)))
print(find_path((3,3), (1,1)))


# ??with cache no return use elif

# C 7 4



# ---------------
# A   I    I C
# ---------------
#    I D	I  B
# ---------------

