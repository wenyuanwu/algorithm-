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

print(look_and_say('2355'))
print(look_and_say('2'))
print(look_and_say(None))
print(look_and_say('23333555'))	