import sys
from itertools import combinations
n=int(sys.stdin.readline())
ability_matrix = tuple(list(map(int, input().split())) for _ in range(n))
for i in range(n):
    ability_matrix[i][i]=0
combi = combinations([i for i in range(n)], n//2)
result=100*20
for i in combi:
    half_matrix=(ability_matrix[j][k] for k in i for j in i)
    half_matrix_other=(ability_matrix[n-1-j][n-1-k] for k in i for j in i)
    result = min(abs(sum(half_matrix)-sum(half_matrix_other)), result)
print(result)
#근데 틀렸음...
