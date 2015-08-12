suits = [[], [], [], []]
i = 0

s = input()

for c in s:
	if c in "DHS":
		i += 1
	else:
		suits[i].append(c)

		if 