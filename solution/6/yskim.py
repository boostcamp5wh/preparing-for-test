#n, k = map(int, sys.stdin.readline().split())
n, k = 5, 8
#belt = {i:{'dura':v,'robo':False} for i,v in enumerate(map(int, sys.stdin.readline().split()))}
belt = {i:{'dura':v,'robo':False} for i,v in enumerate([100,99,60,80,30,20,10,89,99,100])}
zeros, epoch = 0, 0
while zeros<k:
    up, down=((2*n)-(epoch%(2*n)))%(2*n), ((2*n)-(epoch+n)%(2*n))%(2*n) #rotate
    if belt.get(down,{}):                                             #robot down
        if not belt[down]['dura']:
            del belt[down]
        else:
            belt[down]['robo']=False
    keys=sorted(belt.keys(), reverse=True)
    for i in keys:                                                    #robot move
        now, nxt = i, (i+1)%(2*n)
        if belt.get(nxt,{}) and now!=down and belt[now]['robo'] and not belt[nxt]['robo'] and belt[nxt]['dura']:
            # 다음존재O, 현위치내림X, 현위치로봇O, 담위치로봇X, 담위치내구도O
            belt[now]['robo'], belt[nxt]['robo'] = False, True
            belt[nxt]['dura'] -= 1
            if not belt[nxt]['dura']:
                zeros += 1
        if belt[now]['dura']==belt[now]['robo']==0:
            del belt[now]
    if belt.get(up,{}) and not belt[up]['robo'] and belt[up]['dura']: #robot raise
        # 올림위치존재O, 올림위치로봇X, 올림위치내구도O
        belt[up]['dura'] -= 1
        belt[up]['robo'] = True
        if not belt[up]['dura']:
            zeros += 1
    epoch += 1
print(epoch-1)
