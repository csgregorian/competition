n = int(input())

coins = []

for _ in range(n):
	coins.append(int(input()))


dp = [[0 for i in range(n)] for i in range(n)]

for left in range(n):
	for right in range(n-left):
		if left < n-1:
			dp[left+1][right] = max(
				coins[left] + dp[left][right],
				dp[left+1][right]
			)
		if right < n-1:
			dp[left][right+1] = max(
				coins[n-right-1] + dp[left][right],
				dp[left][right+1]
			)

print(max(map(max, dp)))