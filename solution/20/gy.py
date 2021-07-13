token = {
    '(': 1,
    ')': -1,
}

rev_token = {
    '(': ')',
    ')': '(',
}

def solution(p):
    if p == '':
        return p
    
    cnt = token[p[0]]
    is_good = cnt >= 0
    for i in range(1, len(p)):
        cnt += token[p[i]]
        is_good = is_good and cnt >= 0
        if cnt == 0:
            break

    if is_good:
        return p[:i+1] + solution(p[i+1:])
    else:
        return '(' + solution(p[i+1:]) + ')' + \
            ''.join([rev_token[x] for x in p[1:i]])
