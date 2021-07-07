from itertools import combinations as cb
from collections import Counter as ct
def solution(orders, course, answer=[]):
    for j in course:
        combo=ct()
        for order in orders:
            combo += ct(map(lambda x:''.join(sorted(x)), cb(order,j)))
        combo_rev = {}
        m=2
        for i,v in combo.most_common():
            if m<=v:
                m=v
                combo_rev[v] = combo_rev.get(v,[]) + [i]
            else:
                break
        answer.extend(combo_rev.get(max(combo_rev,default=''),[]))
    return sorted(answer)
