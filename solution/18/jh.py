def trans(time):
    h, m, s = map(int, time.split(':'))
    return h*3600 + m*60 + s

def solution(play_time, adv_time, logs):
    alltime = trans(play_time)
    seq = [0 for _ in range(alltime+1)]
    for log in logs:
        start, end = map(trans, log.split('-'))
        seq[start] += 1
        seq[end] -= 1
    adv = trans(adv_time)
    p, cur = 0, seq[0]
    for i in range(1, adv):
        seq[i] += seq[i-1]
        cur += seq[i]
    M = cur
    for i in range(adv, alltime):
        seq[i] += seq[i-1]
        cur += seq[i]-seq[i-adv]
        if cur>M:
            M = cur
            p = i-adv+1
    
    return f'{p//3600:02}:{(p%3600)//60:02}:{p%60:02}'
