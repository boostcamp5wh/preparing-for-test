N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d=[0, 1, 2, 3][N, E, S, W]
board = [list(map(int, input().split())) for _ in range(N)]
state = [[1 if board[i][j] else 0 for j in range(M)] for i in range(N)]
cnt = 0

def clean(i, j):
    global state, cnt
    state[i][j]=1
    cnt+=1

def search(i, j, w):
    if w==0: left, back, way = [i, j-1], [i+1, j], 3
    elif w==1: left, back, way = [i-1, j], [i, j-1], 0
    elif w==2: left, back, way = [i, j+1], [i-1, j], 1
    else: left, back, way = [i+1, j], [i, j+1], 2
    global state, board

    if state[i+1][j] and state[i-1][j] and state[i][j+1] and state[i][j-1] and board[back[0]][back[1]]: return 0
    elif state[i+1][j] and state[i-1][j] and state[i][j+1] and state[i][j-1]: search(back[0], back[1], w)
    elif state[left[0]][left[1]]: search(i, j, way)
    elif not state[left[0]][left[1]]:
        clean(left[0], left[1])
        search(left[0], left[1], way)

clean(r, c)
search(r, c, d)
print(cnt)
