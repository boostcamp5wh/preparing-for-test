def right(u,s=0,i=0):
    while not (s>0 or i>len(u)-1):
        s,i = s+(ord(u[i])-40)*2-1 ,i+1
    return s<=0
def solution(w):
    if not w:
        return ''
    u,v=w[0:2], w[2:]
    while sum([(ord(s)-40)*2-1 for s in u]):
        u,v= u+v[0:2],v[2:]
    return u + solution(v) if right(u) else '('+solution(v)+')'+''.join([chr((ord(s)-40)*40+abs(ord(s)-41)*41) for s in u][1:-1])
