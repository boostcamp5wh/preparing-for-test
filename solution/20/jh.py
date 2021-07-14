def split(s):
    d=0
    for i, c in enumerate(s):
        d = d+1 if c=='(' else d-1
        if not d: return s[:i+1], s[i+1:]
        
def check(s):
    d=0
    for c in s:
        d = d+1 if c=='(' else d-1
        if d<0: return False
    return True

def reverse(s):
    return ''.join([')' if c=='(' else '(' for c in s])

def solution(p):
    if not p: return p
    u, v = split(p)
    if check(u): return u+solution(v)
    else: return '('+solution(v)+')'+reverse(u[1:-1])
