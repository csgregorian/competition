n, t = map(int, input().split())

values = []
weights = []

for _ in range(n):
	v, w = map(int, input().split())
	values.append(v)
	weights.append(w)

dp = [[0 for x in range(n+1)] for y in range(t+1)]
# dp[capacity][limit] is the max score with the given capacity
# and using elements up to but not including limit 

for capacity in range(t+1):
	for item in range(n):
		value = values[item]
		weight = weights[item]

		dp[capacity][item] = dp[capacity][item-1]

		if weight <= capacity:
			dp[capacity][item] = max(
				dp[capacity][item-1], # no item added
				dp[capacity - weight][item-1] + value
			)

print(dp[t][n-1])
