J = int(input())
A = int(input())

sizes = [input() for _ in range(J)]

athletes = [input().split() for _ in range(A)]

requests = 0

for size, num in athletes:
	num = int(num) - 1

	if size == "S":
		if sizes[num] in "SML":
			requests += 1
			sizes[num] = "X"
	elif size == "M":
		if sizes[num] in "ML":
			requests += 1
			sizes[num] = "X"
	elif size == "L":
		if sizes[num] in "L":
			requests += 1
			sizes[num] = "X"
	
print(requests)