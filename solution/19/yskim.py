def solution(s, answer=[]):
    for string in ((s[j*i:j*i+i] for j in range((len(s)//i)+1) if i*j<len(s)) for i in range(1,(len(s)//2)+1)):
        comp=''
        stack=next(string)
        cnt=1
        for letter in string:
            if letter!=stack:
                comp += stack + str(cnt)*(cnt>1)
            cnt = 1 + cnt*(letter==stack)
            stack=letter
        comp += stack + str(cnt)*(cnt>1)
        answer.append(comp)
    return min(map(len,answer)) if answer else 1
