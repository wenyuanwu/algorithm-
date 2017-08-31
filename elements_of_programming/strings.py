# 6.1
# interconvert strings and integers
import functools

def int_to_string(x):
	is_negative = False
	if x < 0: 
	   is_negative = True
	   x = -x 
	str = []
	while x != 0: 
	   str.append(chr(ord('0') + x % 10))
	   x //= 10     
	return ('-'if is_negative else '') + ''.join(reversed(str))   

y = -12300023452
print(int_to_string(y))
print(type(int_to_string(y)))

def string_to_int(str):
    # num = 0
    # # for i in range(len(str)):
    # 	num = num * 10 + (ord(str[i]) - ord('0'))
    # return num 

    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), str[str[0] == '-':], 0) * (-1 if str[0] == '-' else 1)

str_test = "12341243124"
print(string_to_int(str_test))
print(type(string_to_int(str_test)))