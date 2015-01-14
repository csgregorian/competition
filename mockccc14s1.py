name = input()[::-1]
seq = input()
print(len(name) - name.find(seq) if name.find(seq) >= 0 else -1)
