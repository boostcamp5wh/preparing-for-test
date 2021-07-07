N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = A.count(0)
A = [[i, False] for i in A]

step = 0

while cnt < K:
    step+=1
    # rotate
    A[N-1][1] = False
    A.insert(0, A.pop())
    A[N-1][1] = False
    # move
    for i in range(N-2, 0, -1):
        if A[i][1] and A[i+1][0] and not A[i+1][1]:
            A[i][1] = False
            A[i+1][0] -= 1
            if not A[i+1][0]: cnt += 1
            A[i+1][1] = True
    # put
    if A[0][0]:
        A[0][1] = True
        A[0][0] -= 1
        if not A[0][0]: cnt += 1

print(step)
