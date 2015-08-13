# Genotypes are HD, HR, HZ
# (R)ecessive, or (H)eterozygous

def probability_of_dominant(org1, org2):
	code = {
		("HD", "HD"): 1.0,
		("HD", "HZ"): 1.0,
		("HD", "HR"): 1.0,
		("HZ", "HD"): 1.0,
		("HZ", "HZ"): 0.75,
		("HZ", "HR"): 0.5,
		("HR", "HD"): 1,
		("HR", "HZ"): 0.5,
		("HR", "HR"): 0
	}

	return code[(org1, org2)]

hd, hz, hr = map(int, input().split())

orgs = ["HD"] * hd + ["HZ"] * hz + ["HR"] * hr

total = 0
dominant = 0

for a in range(0, len(orgs)):
	for b in range(a+1, len(orgs)):
		total += 1
		dominant += probability_of_dominant(orgs[a], orgs[b])

print(dominant/total)

