K = int(input())

m = int(input())

rounds = [int(input()) for i in range(m)]

friends = list(range(1, K+1))

for r in rounds:
	friends = [friends[i] for i in range(len(friends)) if i % r != r-1]

for f in friends:
	print(f)