import heapq
def solution(n, s, a, b, fares):
    def dijk(start):
        dijk_s = {start:0}
        visit = set()
        q=[(0, start)]
        while q:
            dist, curr = heapq.heappop(q)
            for idx,val in graph[curr].items():
                if (idx not in visit) and (dijk_s.get(idx,float('inf'))>dijk_s.get(curr,0)+graph[curr][idx]):
                    dist = dijk_s.get(curr,0)+graph[curr][idx]
                    dijk_s[idx] = dist
                    heapq.heappush(q, (dist, idx))
                visit.add(curr)
        return dijk_s
    graph={}
    for fare in fares:
        graph[fare[0]] = {**graph.get(fare[0],{}), fare[1]:fare[2]}
        graph[fare[1]] = {**graph.get(fare[1],{}), fare[0]:fare[2]}
    dijk_s, dijk_a, dijk_b = dijk(s), dijk(a), dijk(b)
    return min(dijk_s[m] + dijk_a[m] + dijk_b[m] for m in dijk_s.keys())
