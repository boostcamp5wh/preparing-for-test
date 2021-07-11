def dijkstra(n, start, table):
    shortest_path={i:float('inf') if i!=start else 0 for i in range(1, n+1)}
    visited=set()
    for _ in range(n):
        q=[v for v, _ in sorted(shortest_path.items(), key=lambda x:x[1], reverse=True) if v not in visited]
        cur=q.pop()
        visited.add(cur)
        for dst, cost in table[cur].items():
            shortest_path[dst]=min(shortest_path[dst], shortest_path[cur]+cost)
    return shortest_path

def solution(N, S, A, B, Fares):
    price_table={i:dict() for i in range(1, N+1)}
    [[price_table[a].update({b:cost}), price_table[b].update({a:cost})] for a, b, cost in Fares]
    from_S = dijkstra(N, S, price_table)
    from_A = dijkstra(N, A, price_table)
    from_B = dijkstra(N, B, price_table)

    return min([from_S[to]+from_A[to]+from_B[to] for to in range(1, N+1)])
