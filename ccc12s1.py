J = int(input())

n = 0

for a in range(1, J):
	for b in range(1, a):
		for c in range(1, b):
			n += 1

print(n)

