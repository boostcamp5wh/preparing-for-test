import functools


def solution(sales, links):
    n = len(sales)
    sales = [-1] + sales # index 1 based
    childrens = [[] for _ in range(n+1)]
    for par, child in links:
        childrens[par].append(child)
    
    @functools.lru_cache(maxsize=2*n)
    def dp(idx, optional):
        children_opts = [dp(next_idx, True) for next_idx in childrens[idx]]
        total_opts = sum(children_opts)
        ret = sales[idx] + total_opts
        
        if optional:
            i = -1
            for i, must_idx in enumerate(childrens[idx]):
                ret = min(ret, total_opts - children_opts[i] + dp(must_idx, False))
                
            if i == -1:
                ret = 0
                
        return ret
    
    answer = dp(1, True)
    return answer
