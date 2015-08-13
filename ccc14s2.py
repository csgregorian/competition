N = int(input())

name1 = input().split()
name2 = input().split()

names = dict(zip(name1, name2))

good = True

for key, item in names.items():
	if not (names[key] == item and names[item] == key) or key == item:
		good = False
		break


if good:
	print("good")

else:
	print("bad")