points = int(input())

#Slides from a point
slides = [[] for x in range(points+1)]

#Number of paths to the slide
paths = [0 for x in range(points+1)]
#First point
paths[1] = 1

while True:
	slide = input().split()
	if slide == ['0', '0']:
		break
	slides[int(slide[0])].append(int(slide[1]))

for point in range(1, points+1):
	for dest in slides[point]:
		paths[dest] += paths[point]


print(paths[-1])