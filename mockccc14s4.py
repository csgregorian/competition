N, M = map(int, input().split())

paths = [[] for i in range(N+1)]

for i in range(M):
	a, b = map(int, input().split())
	paths[a].append(b)
	paths[b].append(a)

routes = 0

def go(route):
	global routes
	global paths
	for i in paths[route[-1]]:
		if i not in route:
			if i == N:
				routes += 1
				if routes == 2:
					print("Yes")
					exit()
			else:
				go(route + (i,))

go((1,))

print("No")

