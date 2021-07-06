from collections import deque

n = int(input())
k = int(input())

board = [['E'] * n for _ in range(n)]
board[0][0] = 'S'

apples = [map(int, input().split()) for _ in range(k)]
apples = [[y-1, x-1] for y, x in apples]
for y, x, in apples:
	board[y][x] = 'A'

l = int(input())
turns = [input().split() for _ in range(l)]
turns = [[int(x[0]), x[1]] for x in turns]
turns.reverse()
turns_len = l

dy = [0, 1,  0, -1]
dx = [1, 0, -1,  0]
ld = 'LD'

snakes = deque([(0, 0)])
time = 0
direction = 0
y, x = 0, 0
while True:
	# print('time', time)
	# [print(tmp) for tmp in board]
	time += 1

	next_y = y + dy[direction]
	next_x = x + dx[direction]
	if not (0 <= next_y < n and 0 <= next_x < n):
		# print('out1')
		break

	# print(next_y, next_x)
	if board[next_y][next_x] == 'S':
		# print('out2')
		break

	if board[next_y][next_x] == 'E':
		front_y, front_x = snakes.popleft()
		board[front_y][front_x] = 'E'
	board[next_y][next_x] = 'S'
	snakes.append((next_y, next_x))

	y, x = next_y, next_x

	if turns_len > 0 and turns[-1][0] == time:
		direction += 2 * ld.index(turns[-1][1]) - 1
		direction = (direction + 4) % 4
		turns.pop()
		turns_len -= 1

print(time)
