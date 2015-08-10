n = int(input())
s = input()
s2 = "".join(["#" + i  for i in s]) + "#"

dp = [0 for i in range(len(s2))]

centre = right = 0;

for i in range(len(s2)):
	reverse = centre * 2 - 1

	if i < right:
		dp[i] = min(dp[reverse], right - i)

	while (i + 1 + dp[i] < len(s2) and s2[i+1+dp[i]] == s2[i-1-dp[i]]):
		dp[i] += 1

	if i+dp[i] > right:
		center = i
		right = i + dp[i]

maxdp = 0
maxloc = 0

for i in range(len(dp)):
	if dp[i] > maxdp:
		maxdp = dp[i]
		maxloc = i

print("".join([s2[i] if s2[i] != "#" else "" for i in range(maxloc-maxdp, maxloc+maxdp)]))
print(maxdp)