def solution(s, answer=[]):
    ss = [[] for i in range((len(s)//2))]
    for i in range(1,(len(s)//2)+1):
        for j in range((len(s)//i)+1):
            if i*j<len(s):
                ss[i-1].append(s[j*i:j*i+i])
    for string in ss:
        comp=''
        stack=string[0]
        cnt=0
        for letter in string:
            if letter!=stack:
                comp += stack + str(cnt)*(cnt>1)
            cnt = 1 + cnt*(letter==stack)
            stack=letter
        comp += stack + str(cnt)*(cnt>1)
        answer.append(comp)
    return min(map(len,answer)) if answer else 1
