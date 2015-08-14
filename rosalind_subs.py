string = input()
substring = input()

locations = []

for start in range(0, len(string) - len(substring)):
	if string[start:start+len(substring)] == substring:
		locations.append(str(start + 1))

print(" ".join(locations))