def solution(new_id):
    one_two = [x for x in new_id.lower() if x in 'abcdefghijklmnopqrstuvwxyz0123456789-_.']
    three = []
    for x in one_two:
        if not (x == '.' and len(three) >= 1 and three[-1] == '.'):
            three.append(x)
    three = ''.join(three)
    four = three.strip('.')
    five_six = 'a' if len(four) == 0 else four[:15].strip('.')
    seven = five_six + five_six[-1] * max(3 - len(five_six), 0)
    return seven
