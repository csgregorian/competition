def monkeyLang(word):
	if word == "A":
		return True

	if len(word) < 2:
		return False

	if word[0] == "B" and word[-1] == "S":
		return monkeyLang(word[1:-1])

	# ndex = word.find("N")

	# if ndex not in (-1, 0, len(word)-1):
	# 	return monkeyLang(word[0:ndex]) and monkeyLang(word[ndex+1:])


	valid = False
	for i in range(1, len(word) - 1):
		if word[i] == "N":
			if monkeyLang(word[0:i]) and monkeyLang(word[i+1:]):
				return True



	return False

while True:
	word = input().upper()
	if word == "X":
		break
	else:
		print("YES" if monkeyLang(word) else "NO")



