import heapq

def solution(n, s, a, b, fares):
    edges = [[0] * (n+1) for _ in range(n+1)] # n+1: 1 based index
    for n1, n2, d in fares:
        edges[n1][n2] = d
        edges[n2][n1] = d
    
    def dijkstra(start, edges):
        INIT_VALUE = float('inf')
        min_dists = [INIT_VALUE] * (n+1)
        pq = [(0, start)]
        
        try:
            while True:
                top = None
                while top is None:
                    top = heapq.heappop(pq)
                    if min_dists[top[1]] != INIT_VALUE:
                        top = None

                min_dists[top[1]] = top[0]
                for next_node, dist in enumerate(edges[top[1]]):
                    if dist > 0 and min_dists[next_node] == INIT_VALUE:
                        heapq.heappush(pq, (top[0]+dist, next_node)) 
        except IndexError:
            pass
        
        return min_dists
    
    s_min_dists = dijkstra(s, edges)
    a_min_dists = dijkstra(a, edges)
    b_min_dists = dijkstra(b, edges)

    answer = float('inf')
    for pass_through in range(1, n+1):
        answer = min(answer, s_min_dists[pass_through] + a_min_dists[pass_through] + \
                        b_min_dists[pass_through])
    return answer
