x = [input() for i in range(int(input()))]

for i in x:
	print(int(str(int(i.split()[0][::-1]) + int(i.split()[1][::-1]))[::-1]))

