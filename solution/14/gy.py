import sys
from collections import deque

def rotate(y, x, width):
    for i in range(width):
        for j in range(width):
        	tmp_board[y+j][x+width-1-i] = board[y+i][x+j]

n, q = list(map(int, sys.stdin.readline().rstrip().split()))
b = 1<<n

board = [[0] * (b+2)]
board.extend([[0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0] for _ in range(b)])
board.append([0] * (b+2))
tmp_board = [[0] * (b+2) for _ in range(b+2)]
queries = list(map(int, sys.stdin.readline().rstrip().split()))

total_ice = 0
for i in range(1, b+1):
	for j in range(1, b+1):
		total_ice += board[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for query in queries:
	if query != 0:
		width = 1<<query
		max_pieces = 1 << (n-query)
		for i in range(max_pieces):
			for j in range(max_pieces):
				rotate(i*width+1, j*width+1, width)
	else:
		tmp_board, board = board, tmp_board

	for i in range(1, b+1):
		for j in range(1, b+1):
			board[i][j] = tmp_board[i][j]
			if tmp_board[i][j] > 0:
				ice_nearby = 4
				for d in range(4):
					ny = i + dy[d]
					nx = j + dx[d]
					if tmp_board[ny][nx] == 0:
						ice_nearby -= 1
						if ice_nearby <= 2:
							break
				if ice_nearby <= 2:
					board[i][j] -= 1
					total_ice -= 1

	if total_ice == 0:
		break

def bfs(i, j):
	que = deque()
	que.append((i, j))
	tmp_board[i][j] = False

	ice_size = 1
	while len(que) > 0:
		i, j = que.popleft()

		for d in range(4):	
			ny = i + dy[d]
			nx = j + dx[d]
			if board[ny][nx] > 0 and tmp_board[ny][nx]:
				tmp_board[ny][nx] = False
				que.append((ny, nx))
				ice_size += 1

	return ice_size

tmp_board = [[True] * (b+2) for _ in range(b+2)]
total_ice = 0
largest_ice = 0
for i in range(1, b+1):
	for j in range(1, b+1):
		total_ice += board[i][j]
		if tmp_board[i][j] and board[i][j] > 0:
			largest_ice = max(bfs(i, j), largest_ice)
if largest_ice == 1:
	largest_ice = 0
print(total_ice)
print(largest_ice)
