nums = []

for i in range(int(input())):
	nums.append(int(input()))

for i in nums:
	x = sum(z if i % z == 0 else 0 for z in range(1, i))
	if x == i:
		print(i, "is a perfect number.")
	elif x > i:
		print(i, "is an abundant number.")
	else:
		print(i, "is a deficient number.")