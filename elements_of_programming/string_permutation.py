def str_permutation(str):
    # write the body of your function here
    if len(str) <= 1:
        return {[str]}
    else:
        result_set = set()
    	permutation("", str, str, result_set)
	return result_set

def permutation(sub_str, rest_str, str, result_set):
    if len(sub_str) == len(str):
        result_set.add(sub_str)
    else:
        for i in range(len(rest_str)):
            permutation(sub_str + rest_str[i], rest_str[:i] + rest_str[i+1:], str, result_set)
            

        
# run your function through some test cases here
# remember: debugging is half the battle!
print str_permutation('abcd')
