def solution(info, query, answer = []):
    mp={0:'lang',1:'end',2:'year',3:'food',4:'score'}
    info=[{mp[j]:v for j,v in enumerate(inf.split())} for i, inf in enumerate(info)]
    for que in query:
        que=que.split(' and ')
        q, score = que[-1].split()
        que=que[:-1] + [q]
        que={mp[i]:c for i,c in enumerate(que) if c!='-'}
        confirm=0
        for i in info:
            match=1
            if int(score)>int(i['score']):
                match=0
            else:
                for q in que:
                    if que[q] != i[q]:
                        match=0
                        break
            confirm += 1*match
        answer.append(confirm)
    return answer
