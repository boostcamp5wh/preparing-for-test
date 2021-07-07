n=int(input())
table=[[0, 0, 0]]
for _ in range(n):
    t, p = map(int, input().split())
    table.append([t, p, 0])

for i in range(n):
    current_benefit = table[i][2]
    table[i+1][2]=max(table[i+1][2], table[i][2])
    next_job = table[i+1]
    if i+next_job[0]<n+1: table[i+next_job[0]][2] = max(current_benefit + next_job[1], table[i+next_job[0]][2])

print(table[-1][2])
