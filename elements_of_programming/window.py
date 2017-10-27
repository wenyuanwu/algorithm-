import heapq

S = "EAFGHCDBEFGCAKBLMCNADEC"
SET = {"A", "B", "C"}

def shortest_string(s, set_input):
	hm = {}
	for i in range(len(s)):
		if s[i] in set_input and hm.get(s[i]):
			hm[s[i]].append(i)
		elif s[i] in set_input:
			hm[s[i]] = [i]

	l = [hm[k][0] for k in hm.keys()]
	current_min = min(l)
	current_max = max(l)
	min_len = current_max - current_min
	global_min = min(l)
	global_max = max(l)
	heapq.heapify(l)

	current_index = l[0]
	current_key = s[current_index]
	next_index = hm[current_key].index(current_index) + 1

	while next_index < len(hm[current_key]):
		heapq.heappushpop(l,hm[current_key][next_index])
		if hm[current_key][next_index] > current_max:
			current_max = hm[current_key][next_index]
		current_index = l[0]
		current_key = s[current_index]
		next_index = hm[current_key].index(current_index) + 1

		current_min = l[0]
		if current_max - current_min < min_len:
			min_len = current_max - current_min
			global_min = current_min
			global_max = current_max

	return S[global_min: global_max + 1]

print(shortest_string(S, SET))


