seq = input()

decode = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}

mod = []
val = []

for i in range(0, len(seq), 2):
	A = int(seq[i])
	R = decode[seq[i+1]]

	mod.append(A)
	val.append(R)

for v in range(len(val) - 1):
	if val[v] < val[v+1]:
		val[v] *= -1

s = 0

for i in range(len(mod)):
	s += mod[i] * val[i]

print(s)
