def solution(n, k, cmd,u = {'U':-1, 'D':1,0:'X',1:'O'},answer=''):
    def move(how):
        nonlocal k
        if how:
            val = 1 if how>0 else -1
            while how:
                k+=val
                if table[k]:
                    how -= val
    mov,dele,table = 0, [], [1]*n
    for c in cmd:
        if len(c)==3:
            mov += next(map(lambda x,y: u[x]*int(y), *c.split()))
        else:
            move(mov)
            mov=0
            if c=='C':
                table[k] = 0
                dele.append(k)
                final = True
                for i in range(k+1,n):
                    if table[i]:
                        final=False
                        break
                move(-1) if final else move(1)
            else:
                table[dele.pop()] = 1
    for i in table:
        answer += u[i]
    return answer
    
    왜 런타임..에러?
    정확성
    test 5 ~ 22 Runtime Error
    test 29, 30 Fail
    효율성
    test 1~5 Fail
    test 7 Runtime Error
    test8 Time Exceed
