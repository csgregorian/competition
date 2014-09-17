def pattern(num, max0, max1):
	if len(num) == max0 + max1:
		print(num)
		return
	if num.count("1") < max1:
		pattern(num+"1", max0, max1)
	if num.count("0") < max0:
		pattern(num+"0", max0, max1)

x = []

for i in range(int(input())):
	n, k = map(int, input().split())
	x.append((n, k))

for i in x:
	n, k = i
	print("The bit patterns are")
	pattern("", n-k, k)
	print("")

