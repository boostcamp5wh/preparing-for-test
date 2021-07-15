def check_person(y, x, place):
    # O: 확인 안됨, B: 이전에 확인, C: 현재 확인, X: 중심
    #   O
    #  OOB
    # OOXOO
    #  COO
    #   O
    if y < 4 and 0 < x and place[y+1][x-1] == 'P' and \
        (place[y+1][x] != 'X' or place[y][x-1] != 'X'):
        return False
        
    #   B
    #  BBO
    # BBXCC
    #  OCC
    #   C
    stack = []
    next_stack = [(y, x)]
    for _ in range(2):
        stack = next_stack
        next_stack = []
        for y, x in stack:
            if y < 4:
                if place[y+1][x] == 'P':
                    return False
                elif place[y+1][x] == 'O':
                    next_stack.append((y+1, x))

            if x < 4:
                if place[y][x+1] == 'P':
                    return False
                elif place[y][x+1] == 'O':
                    next_stack.append((y, x+1))
    return True

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and check_person(i, j, place) == False:
                return 0
    return 1
    

def solution(places):     
    return [check(place) for place in places]
