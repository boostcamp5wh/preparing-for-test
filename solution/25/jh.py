answer = 80

def cntl(distmap, board, i, j):
    I, J = i, j
    if i>0:
        i-=1
        while i>0 and board[i][j]==0: i-=1
        distmap[i][j]=min(distmap[i][j], distmap[I][J]+1)
        i, j = I, J
    if i<3:
        i+=1
        while i<3 and board[i][j]==0: i+=1
        distmap[i][j]=min(distmap[i][j], distmap[I][J]+1)
        i, j = I, J
    if j>0:
        j-=1
        while j>0 and board[i][j]==0: j-=1
        distmap[i][j]=min(distmap[i][j], distmap[I][J]+1)
        i, j = I, J
    if j<3:
        j+=1
        while j<3 and board[i][j]==0: j+=1
        distmap[i][j]=min(distmap[i][j], distmap[I][J]+1)
    return distmap

def dijk(origin, xy):
    r, c = xy
    distmap=[[6 for _ in range(4)] for _ in range(4)]
    distmap[r][c]=0
    visited=set()
    for _ in range(16):
        q=6
        for a in range(4):
            for b in range(4):
                if (a, b) not in visited and distmap[a][b]<q:
                    i, j = a, b
                    q=distmap[a][b]
        visited.add((i, j))
        distmap = cntl(distmap, origin, i, j)
        if i>0: distmap[i-1][j] = min(distmap[i][j]+1, distmap[i-1][j])
        if i<3: distmap[i+1][j] = min(distmap[i][j]+1, distmap[i+1][j])
        if j>0: distmap[i][j-1] = min(distmap[i][j]+1, distmap[i][j-1])
        if j<3: distmap[i][j+1] = min(distmap[i][j]+1, distmap[i][j+1])
    return distmap

def calc(board, start, to):
    A = dijk(board, start)
    s_to_pre=A[to[0][0]][to[0][1]]
    s_to_post=A[to[1][0]][to[1][1]]
    return 2+s_to_pre+dijk(board, to[0])[to[1][0]][to[1][1]],\
           2+s_to_post+dijk(board, to[1])[to[0][0]][to[0][1]]

def dfs(pos, _board, now, _visited, to, count):    
    if len(_visited)==len(pos):
        global answer
        answer=min(answer, count)
        return 0
    toA, toB = calc(_board, now, pos[to])
    _board[pos[to][0][0]][pos[to][0][1]]=0
    _board[pos[to][1][0]][pos[to][1][1]]=0
    for nxt in pos.keys():
        if nxt not in _visited:
            dfs(pos, _board, pos[to][1], _visited|set([to]), nxt, count+toA)
            dfs(pos, _board, pos[to][0], _visited|set([to]), nxt, count+toB)

def solution(board, r, c):
    pos={}
    for k in range(16):
        i, j = k//4, k%4
        if board[i][j] and board[i][j] in pos: pos[board[i][j]].append([i, j])
        elif board[i][j] and board[i][j] not in pos: pos[board[i][j]]=[[i, j]]
    [dfs(pos, board, [r, c], set(), to, 0) for to in pos.keys()]
    global answer
    return answer
