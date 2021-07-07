n = int(input())

ar = [map(int, input().split()) for _ in range(n)]

profits = [0] * (n+1)
for i in range(n-1, -1, -1):
	work_len, pay = ar[i]
	profits[i] = profits[i+1]
	if i + work_len <= n:
		profits[i] = max(profits[i], pay + profits[i+work_len])
print(profits[0])
