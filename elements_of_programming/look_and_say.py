def look_and_say(s):

	if not s:
		return ""

	if len(s) == 1:
		return "1" + s

	result_arr = []
	count = 1

	for i in range(len(s)):
		if i < len(s) - 1:
			if s[i] == s[i + 1]:
				count += 1
				continue
			else:	
				result_arr.append(str(count))
				result_arr.append(s[i])
				count = 1
		else:
			if s[i] == s[i -1]:
				result_arr.append(str(count))
				result_arr.append(s[i])
			else:
				result_arr.append("1")
				result_arr.append(s[i])
							

	return "".join(result_arr)


def reverse(str):
	result_str = ""
	for i in range(0, len(str) -1, 2):
			j = int(str[i])
			if str[i -1] == str[i + 1]:
				raise "Invalid input"
			else:  
				result_str += j * str[i + 1]

	return result_str		

print(reverse("121325"))
print(reverse("2222"))
# print(look_and_say('2355'))
# print(look_and_say('2'))
# print(look_and_say(None))
# print(look_and_say('23333555'))	