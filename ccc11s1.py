text = ""

for _ in range(int(input())):
	text += input()

text = text.lower()

T = text.count("t")
S = text.count("s")

if (T > S):
	print("English")
else:
	print("French")