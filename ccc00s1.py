q = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

turns = 0

while q > 0:
	q -= 1

	if turns % 3 == 0:
		m1 += 1
		if m1 == 35:
			q += 30
			m1 = 0
	elif turns % 3 == 1:
		m2 += 1
		if m2 == 100:
			q += 60
			m2 = 0
	else:
		m3 += 1
		if m3 == 10:
			q += 9
			m3 = 0

	turns += 1

print("Martha plays %d times before going broke." % turns)