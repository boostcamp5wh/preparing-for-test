def cp_permutations(ar):
	n = len(ar)
	while True:
		yield ar

		idx = n-1
		while idx >= 1 and ar[idx-1] >= ar[idx]:
			idx -= 1

		if idx == 0:
			return

		switch = n-1
		while ar[idx-1] >= ar[switch]:
			switch -= 1

		ar[idx-1], ar[switch] = ar[switch], ar[idx-1]
		ar[idx:n] = ar[n-1:idx-1:-1]

n = int(input())

ar = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
	for j in range(i+1, n):
		ar[i][j] += ar[j][i]
		ar[j][i] = 0

best = 200 * n
for candidate in cp_permutations([0]*(n//2) + [1]*(n//2)):
	cur_sum = 0
	other_sum = 0
	cur_team = []
	other_team = []
	for i, v in enumerate(candidate):
		if v == 1:
			for member in cur_team:
				cur_sum += ar[member][i]
			cur_team.append(i)
		else:
			for member in other_team:
				other_sum += ar[member][i]
			other_team.append(i)

	best = min(best, abs(other_sum - cur_sum))
print(best)
