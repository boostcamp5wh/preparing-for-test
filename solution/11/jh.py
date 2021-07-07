from copy import deepcopy

N, M = map(int, input().split())
field=[list(map(int, input().split())) for _ in range(N)]
pos=[[i, j] for i in range(N) for j in range(M) if field[i][j]==2]

def spread(F, i, j):
    global N, M
    if i>0 and not F[i-1][j]:
        F[i-1][j]=2
        F=spread(F, i-1, j)
    if i<N-1 and not F[i+1][j]:
        F[i+1][j]=2
        F=spread(F, i+1, j)
    if j>0 and not F[i][j-1]:
        F[i][j-1]=2
        F=spread(F, i, j-1)
    if j<M-1 and not F[i][j+1]:
        F[i][j+1]=2
        F=spread(F, i, j+1)
    return F

def pick(A, B, C, F):
    F[A[0]][A[1]]=1
    F[B[0]][B[1]]=1
    F[C[0]][C[1]]=1
    global pos
    for r, c in pos:
        F=spread(F, r, c)
    return F

area=0
case=[(i, j) for i in range(N) for j in range(M) if field[i][j]==0]
if len(case)>3:
    for i in range(len(case)-2):
        for j in range(i+1, len(case)-1):
            for k in range(j+1, len(case)):
                A, B, C = case[i], case[j], case[k]
                F=deepcopy(field)
                result=pick(A, B, C, F)
                area=max(area, sum([result[row].count(0) for row in range(N)]))
    print(area)
else: print(0)
