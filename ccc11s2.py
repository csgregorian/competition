n = int(input())

r = [input() for _ in range(n)]
a = [input() for _ in range(n)]

s = 0

for i in range(n):
	if r[i] == a[i]:
		s += 1

print(s)