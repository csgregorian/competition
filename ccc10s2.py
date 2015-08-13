k = int(input())

codes = {}

for _ in range(k):
	letter, code = input().split()
	codes[code] = letter

seq = input()
answer = ""

start = 0
end = 1

while end <= len(seq):
	if seq[start:end] in codes.keys():
		answer += codes[seq[start:end]]
		start, end = end, end + 1
	else:
		end += 1

print(answer)