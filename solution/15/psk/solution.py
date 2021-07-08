from itertools import combinations as combi

def solution(orders, course):
    answer = []
    d1 = {}
    d2 = {}
    for order in orders:
        l = len(order)
        order=sorted(order)
        for i in range(2,l+1):
            for j in combi(order,i):
                
                key = ''.join(j)
                d1[key] = d1.get(key,0)+1
    
    for k,v in d1.items():
        if len(k) in course and v>=2:
            t = d2.get(len(k),list())
            t.append((k,v))
            d2[len(k)]=t
            
    for k,v in d2.items():
        v.sort(key=lambda x : -x[1])
        _max = v[0][1]
        
        for i in v:
            if i[1]==_max:
                answer.append(i[0])
            else:
                break
    return sorted(answer)