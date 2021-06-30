import sys
from itertools import combinations
n=int(sys.stdin.readline())
ability_matrix = tuple(list(map(int, input().split())) for _ in range(n))
combi = combinations([i for i in range(n)], n//2)
result=100*20
for c in range(len(combi)//2):
    team_a=sum(ability_matrix[i][j] for i in combi[c] for j in combi[c])
    team_b=sum(ability_matrix[i][j] for i in combi[len(combi)-c-1] for j in combi[len(combi)-c-1])
    result = min(abs(team_a-team_b),result)
print(result)
