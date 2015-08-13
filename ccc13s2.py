W = int(input())

N = int(input())

cars = [int(input()) for _ in range(N)]

T = 0

weight = 0

for i in range(N):
	if (i > 3):
		weight -= cars[i - 4]
	weight += cars[i]

	if (weight <= W):
		T += 1
	else:
		break

print(T)