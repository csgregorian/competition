s1 = input()
s2 = input()

def hamming(s1, s2):
	assert(len(s1) == len(s2))

	dist = 0

	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

print(hamming(s1, s2))