n = 8

max_id = ""
max_gc = -1.0

for _ in range(n):
	dna_id = input()
	dna_string = input()

	gc_count = dna_string.count("G") + dna_string.count("C")
	gc = gc_count / len(dna_string)

	if gc > max_gc:
		max_gc = gc
		max_id = dna_id

print(max_id)
print(max_gc)
