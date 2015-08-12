Y = int(input())

distinct = False

while not distinct:
	Y += 1

	for i in str(Y):
		if str(Y).count(i) > 1:
			break
	else:
		distinct = True

print(Y)