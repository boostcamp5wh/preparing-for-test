from collections import defaultdict
from itertools import permutations

dy = [ 0, 0, -1, 1]
dx = [-1, 1,  0, 0]
def get_min_moves(start, end, board):
    count = -1
    que = []
    next_que = []
    been = set()
    found = False

    def add_next_ele(ele):
        if ele not in been:
            been.add(ele)
            next_que.append(ele)

    in_board = lambda y, x: 0 <= next_y < 4 and 0 <= next_x < 4

    add_next_ele(start)
    
    while not found:
        que, next_que = next_que, []
        count += 1
        for cur_y, cur_x in que:
            if (cur_y, cur_x) == end:
                found = True
                break

            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                if in_board(next_y, next_x):
                    add_next_ele((next_y, next_x))

                while in_board(next_y, next_x) and board[next_y][next_x] == 0:
                    next_y += dy[i]
                    next_x += dx[i]

                if not in_board(next_y, next_x):
                    next_y -= dy[i]
                    next_x -= dx[i]

                add_next_ele((next_y, next_x))

    return count

def solve(cur, idx, order, board):
    if idx == order_len:
        return 0
    
    cur_card = order[idx]
    card_order = cards[cur_card]

    common_sum = 2
    tmp = [
        get_min_moves(cur, card_order[i], board) + get_min_moves(card_order[i], card_order[1-i], board) for i in range(2)
    ]
    
    for pos_y, pos_x in card_order:
        board[pos_y][pos_x] = 0

    ret = min(tmp[i] + solve(card_order[1-i], idx+1, order, board) for i in range(2))

    for pos_y, pos_x in card_order:
        board[pos_y][pos_x] = cur_card
        
    return ret + common_sum

cards = defaultdict(list)
order_len = None
def solution(board, r, c):
    global order_len

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))

    order_len = len(cards.keys())
    answer = float('inf')
    for order in permutations(cards.keys()):
        answer = min(answer, solve((r, c), 0, order, board))
    
    return answer
