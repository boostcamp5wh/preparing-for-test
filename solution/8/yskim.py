from sys import stdin as l
from collections import deque as q
d=(-1,0,1,0)
y=1
n=int(l.readline())
mat=[[0,*[--bool(i%(n+1))]*n,0] for i in range(n+2)]
n=int(l.readline())
ap=[list(map(int,l.readline().split())) for _ in range(n)]
for a in ap:
    mat[a[0]][a[1]]=2
n=int(l.readline())
mv=q(list(l.readline().split()) for _ in range(n))
mv.append(['0','D'])
k=mv.popleft()
time=0
r,c=1,1
s=q([(1, 1)])
while mat[r][c]:
    if int(k[0])==time:
        y=((2*(k[1]=='D'))-1+y)%4
        k=mv.popleft()
    old=mat[r][c]
    if mat[r][c]==1:
        ro, co = s.popleft()    
        mat[ro][co]=1
    mat[r][c]=0
    s.append(((r,c)))
    r, c = r+d[y], c+d[-y-1]
    time += 1
print(time)
