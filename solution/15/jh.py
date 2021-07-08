from itertools import combinations as combo

def solution(orders, course):
    dic=dict()
    for n in course:
        for order in orders:        
            for cs in combo(order, n):
                menu=''.join(sorted(cs))
                if menu in dic: dic[menu]+=1
                else: dic[menu]=1
                  
    answer={i:dict() for i in course}
    for menu, cnt in dic.items():
        if cnt<2: continue
        if answer[len(menu)].keys():
            most=list(answer[len(menu)].keys())[0]
            if cnt>most:
                del answer[len(menu)][most]
                answer[len(menu)][cnt]=[menu]
            elif cnt==most: answer[len(menu)][cnt].append(menu)
        else: answer[len(menu)][cnt]=[menu]
          
    sets=[]
    for k, v in answer.items():
        if v: sets.extend(answer[k][list(v.keys())[0]])
          
    return sorted(sets)
