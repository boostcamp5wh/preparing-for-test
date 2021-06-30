N=int(input())
board=[[0 if i not in (0, N+1) and j not in (0, N+1) else 1 for j in range(N+2)] for i in range(N+2)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i][j]='A'
L=int(input())

def turn(D, C, i, L):
    nxt=0
    if D==2: nxt = 4 if C else 6
    elif D==4: nxt = 8 if C else 2
    elif D==6: nxt = 2 if C else 8
    elif D==8: nxt = 6 if C else 4

    if i<L:
        cmd = input().split()
        return nxt, int(cmd[0]), 1 if cmd[1]=='L' else 0
    else: return nxt, None, None

def move_head(head, D):
    if D==2: head[0]-=1
    elif D==4: head[1]-=1
    elif D==6: head[1]+=1
    elif D==8: head[0]+=1
    return head

def move_tail(Q, board):
    i, j = Q.pop(0)
    board[i][j]=0

time = 0
head = [1, 1]
D = 6 # U2 L4 R6 D8
Q = [[1, 1]]
cmd = input().split()
X, C = int(cmd[0]), 1 if cmd[1]=='L' else 0
board[head[0]][head[1]] = 1
i=0

while 1:
    time+=1
    head=move_head(head, D)
    Q.append([head[0], head[1]])
    if board[head[0]][head[1]] == 1: break
    elif board[head[0]][head[1]] != 'A': move_tail(Q, board)
    board[head[0]][head[1]] = 1

    if time==X:
        i+=1
        D, X, C = turn(D, C, i, L)

print(time)
