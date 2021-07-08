from itertools import combinations as cb
from collections import Counter as ct
def solution(orders, course, answer=[]):
    for j in course:
        combo=ct()
        for order in orders:
            combo += ct(map(lambda x:''.join(sorted(x)), cb(order,j)))
        combo_rev = {}
        for i,v in combo.items():
            combo_rev[v] = combo_rev.get(v,[]) + [i]*bool(v-1)
        answer.extend(combo_rev.get(max(combo_rev,default=''),[]))
    return sorted(answer)
