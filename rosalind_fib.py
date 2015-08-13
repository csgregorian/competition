n, k = map(int, input().split())

dp = [(0, 0)] * (n + 1)
dp[0] = (1, 0)

for month in range(1, n + 1):
	dp[month] = (dp[month-1][1] * k, dp[month-1][0] + dp[month-1][1])

print(dp[month][1])