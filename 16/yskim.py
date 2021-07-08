def solution(info, query, info_mat = {}, answer = []):
    mp = {'p':1, 'a':2, 'y':4, 'r':1,'u':1,'e':2,'h':1,'i':2,' ':3}
    for inf in info:
        lang, bf, nior, food, score = inf.split()
        for la in (mp[lang[1]], 7):
            for b in (mp[bf[1]],3):
                for ni in (mp[nior[1]],3):
                    for fo in (mp[food[1]],3):
                        clas = (la<<6) + (b<<4) + (ni<<2) + fo
                        # info_mat[clas] = info_mat.get(clas,[]) + [int(score)]
                        info_mat[clas] = info_mat.get(clas,[])
                        info_mat[clas].append(int(score))
    [info_mat[i].sort() for i in info_mat]
    for que in query:
        que = que.split('and ')
        q, score = que[-1].split()
        clas = ((7 if (que[0][1]==' ') else mp[que[0][1]])<<6) + (mp[que[1][1]]<<4) + (mp[que[2][1]]<<2) + mp[(q+' ')[1]]
        mat = info_mat.get(clas,[])
        f, l = 0, len(mat)-1
        while f<=l:
            m = (f+l)//2
            if mat[m]>=int(score):
                l=m-1
            else:
                f=m+1
        answer.append(len(mat) - f)
    return answer

#(11, 12)줄 대신 10줄 쓰면 시간초과. 10줄 대신 (11, 12)줄 처럼 append 를 써야 시간내에 통과
# sum 도 2d-list 를 flatten 할 때, sum(list,[]) 하면 편하게 list를 풀어 슬 수 있다. 그러나 list = [] + [] 는 느리기 때문에 안쓰는 것 처럼 이것도 그런듯 하다.
#10줄 처럼 쓰면      테스트 9 〉	통과 (217.16ms, 13.3MB), 효율성 다 시간초과
#11,12 줄 처럼 쓰면  테스트 9 〉	통과 (53.28ms, 13.4MB)
# 효율성
# 테스트 1 〉	통과 (1088.95ms, 67.9MB)
# 테스트 2 〉	통과 (1089.28ms, 67.7MB)
# 테스트 3 〉	통과 (1142.86ms, 67.5MB)
# 테스트 4 〉	통과 (1135.87ms, 68.8MB)
