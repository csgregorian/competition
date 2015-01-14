R, C = map(int, input().split())

rows = [tuple(map(int, input().split())) for _ in range(R)]

N = int(input())

def sort(col):
	global rows
	col -= 1
	nums = set()
	for row in rows:
		nums.add(row[col])
	nums = sorted(list(nums))

	newrows = []

	for i in nums:
		for row in rows:
			if row[col] == i:
				newrows.append(row)

	rows = newrows

for i in range(N):
	sort(int(input()))

for row in rows:
	print(' '.join(map(str, row)))

