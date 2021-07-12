def stoi(s : str):
    return int(s[0:2])*3600+int(s[3:5])*60+int(s[6:8])

def numzfill(x:int):
    if x<10:
        return '0'+str(x)
    return str(x)

def itos(t : int):
    ret = numzfill(t//3600)+":"
    t%=3600
    ret+=numzfill(t//60)+":"
    t%=60
    return ret+numzfill(t)

def solution(play_time, adv_time, logs):
    answer = None
    pt,at=stoi(play_time),stoi(adv_time)
    d = [0]*3600001
    
    for log in logs:
        st = stoi(log[:8])
        en = stoi(log[9:17])
        d[st]+=1
        d[en]-=1
        
    # 누적 재생시간 계산
    for i in range(1,360001):
        d[i]+=d[i-1]
        
    mxval,curval,mxtime = 0,0,0
    # 누적 재생시간이 가장 많은 곳 계산
    for i in range(at):
        curval+=d[i]
        
    mxval=curval
    for i in range(1,360001-at):
        curval=curval-d[i-1]+d[i+at-1]
        if curval>mxval:
            mxval = curval
            mxtime=i
    
    return itos(mxtime)