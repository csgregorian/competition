d, e, w = int(input()), int(input()), int(input())

a = 0
b = 0

a += max(0, d-100) * 25
a += e * 15
a += w * 20

b += max(0, d-250) * 45
b += e * 35
b += w * 25

a = float(a)/100
b = float(b)/100

print("Plan A costs %.2f" % a)
print("Plan B costs %.2f" % b)

if a == b:
	print("Plan A and B are the same price.")
elif a > b:
	print("Plan B is cheapest.")
elif a < b:
	print("Plan A is cheapest.")