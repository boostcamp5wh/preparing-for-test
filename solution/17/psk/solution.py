def solution(n, s, a, b, fares):
    answer = 40000002
    inf=20000000
    d=[[20000000 for col in range(n)] for row in range(n)]
    
    for i in range(n):
        d[i][i]=0

    for fare in fares:
        p1=fare[0]-1
        p2=fare[1]-1
        d[p2][p1]=fare[2]
        d[p1][p2]=fare[2]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][i] + d[i][k],d[j][k])
    
    for k in range(n):
        answer=min(d[s-1][k]+d[k][a-1]+d[k][b-1],answer)
    
    return answer