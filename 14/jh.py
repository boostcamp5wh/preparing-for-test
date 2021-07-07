from copy import deepcopy as dc
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N, Q = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

def rotate(field, N, l):
    tmp = dc(field)
    base_r, base_c = 2**(l-1)-0.5, 2**(l-1)-0.5
    for rstep in range(0, 2**N, 2**l):
        for cstep in range(0, 2**N, 2**l):
            Or, Oc = base_r+rstep, base_c+cstep
            for i in range(int(Or+0.5-2**(l-1)), int(Or+0.5+2**(l-1))):
                for j in range(int(Oc+0.5-2**(l-1)), int(Oc+0.5+2**(l-1))):
                    r, c = (i-0.5)-Or, (j+0.5)-Oc
                    r, c = int(c), int(-r)
                    r, c = int(Or+r), int(Oc+c)
                    field[r][c] = tmp[i][j]

def melt(field, N):
    tmp=[]
    for i in range(2**N):
        for j in range(2**N):
            if field[i][j]:
                cnt=0
                if i>0 and field[i-1][j]: cnt+=1
                if i<2**N-1 and field[i+1][j]: cnt+=1
                if j>0 and field[i][j-1]: cnt+=1
                if j<2**N-1 and field[i][j+1]: cnt+=1
                if cnt<3: tmp.append([i, j])
    for i, j in tmp:
        field[i][j]-=1

def dfs(i, j, n):
    global field, visited, num, N
    visited[i][j]=1
    if i>0 and field[i-1][j] and not visited[i-1][j]: n=max(dfs(i-1, j, n+1), n)
    if j>0 and field[i][j-1] and not visited[i][j-1]: n=max(dfs(i, j-1, n+1), n)
    if i<2**N-1 and field[i+1][j] and not visited[i+1][j]: n=max(dfs(i+1, j, n+1), n)
    if j<2**N-1 and field[i][j+1] and not visited[i][j+1]: n=max(dfs(i, j+1, n+1), n)
    return n

for l in L:
    if l: rotate(field, N, l)
    melt(field, N)
print(sum([sum(row) for row in field]))
visited=[[0 for _ in range(2**N)] for _ in range(2**N)]
num=0
for i in range(2**N):
    for j in range(2**N):
        if field[i][j] and not visited[i][j]: num=max(dfs(i, j, 1), num)
        else: visited[i][j]=1
print(num)
