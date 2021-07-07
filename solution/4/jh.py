from itertools import combinations as comb
from sys import stdin

n=int(stdin.readline())
stat=[list(map(int, stdin.readline().split())) for _ in range(n)]
dif=8910

for team in comb([i for i in range(1, n)], n//2-1):
    teamB=[i for i in range(1, n) if i not in team]
    teamA=[0]+list(team)
    A, B = 0, 0

    for i, a in enumerate(teamA[:-1]):
        for b in teamA[i+1:]:
            A += (stat[a][b] + stat[b][a])

    for i, a in enumerate(teamB[:-1]):
        for b in teamB[i+1:]:
            B += (stat[a][b] + stat[b][a])

    dif=min(abs(A-B), dif)

print(dif)
