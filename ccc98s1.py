n = int(input())

for _ in range(n):
	s = input()
	s_list = s.split()
	for i in range(len(s_list)):
		if len(s_list[i]) == 4:
			s_list[i] = "****"

	print(" ".join(s_list) + "\n")