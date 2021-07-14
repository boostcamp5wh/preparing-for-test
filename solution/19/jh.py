def solution(s):
    answer = len(s)
    for l in range(1, len(s)//2+1):
        i, compstr = 0, 0
        while i<len(s)-l+1:
            if s[i:i+l]==s[i+l:i+l+l]:
                cnt=1
                compstr+=l
                while s[i:i+l]==s[i+l:i+l+l]:
                    cnt+=1
                    i+=l
                compstr+=len(str(cnt))
            else: compstr+=l
            i+=l
        if i<len(s): compstr+=len(s[i:])
        answer=min(answer, compstr)
    return answer
