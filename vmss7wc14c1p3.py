def sieve(n):
	primes = []
	sieve = [True] * (n + 1)

	for p in range(2, n+1):
		if sieve[p]:
			primes.append(p)
			for i in range(p ** 2, n + 1, p):
				sieve[i] = False

	return primes

n, k = map(int, input().split())

primes = sieve(n)

dp = [65535 for i in range(n+1)]
for prime in primes:
	dp[prime] = 1

for i in range(4, n+1):
	for prime in primes:
		if prime >= i:
			break
		dp[i] = min(dp[i], dp[i-prime] + 1)

s = 0

for i in dp:
	if i == k:
		s += 1

print(s)
