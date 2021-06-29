N=int(input())
dic=dict()
for i in range(N**2):
    P=list(map(int, input().split()))
    dic[P[0]]=P[1:]
board=[[None for _ in range(N)] for _ in range(N)]

def search(like, board):
    N=len(board)
    candidates=[]
    cnt_like, cnt_empty = 0, 0
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                tmp_like, tmp_empty=0, 0
                if i>0: # up limit
                    if not board[i-1][j]: tmp_empty+=1
                    elif board[i-1][j] in like: tmp_like+=1
                if i<N-1: # down limit
                    if not board[i+1][j]: tmp_empty+=1
                    elif board[i+1][j] in like: tmp_like+=1
                if j>0: # left limit
                    if not board[i][j-1]: tmp_empty+=1
                    elif board[i][j-1] in like: tmp_like+=1
                if j<N-1: # right limit
                    if not board[i][j+1]: tmp_empty+=1
                    elif board[i][j+1] in like: tmp_like+=1

                if tmp_like>cnt_like:
                    cnt_like=tmp_like
                    cnt_empty=tmp_empty
                    candidates=[[i, j]]
                elif tmp_like==cnt_like:
                    if tmp_empty>cnt_empty:
                        cnt_empty=tmp_empty
                        candidates=[[i, j]]
                    elif cnt_empty==tmp_empty: candidates.append([i, j])
    
    return sorted(candidates, key=lambda x:(x[0], x[1]))[0]

def score(cnt):
    if cnt==1: return 1
    elif cnt==2: return 10
    elif cnt==3: return 100
    elif cnt==4: return 1000
    else: return 0

for num, like in dic.items():
    i, j = search(like, board)
    board[i][j]=num

prize=0
for i in range(N):
    for j in range(N):
        cnt=0
        num=board[i][j]
        if i>0 and board[i-1][j] in dic[num]: cnt+=1
        if i<N-1 and board[i+1][j] in dic[num]: cnt+=1
        if j>0 and board[i][j-1] in dic[num]: cnt+=1
        if j<N-1 and board[i][j+1] in dic[num]: cnt+=1

        prize+=score(cnt)

print(prize)
