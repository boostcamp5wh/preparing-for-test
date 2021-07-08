N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
e=1023
blocks=[
    [[e, e, e, e]], [[e],[e],[e],[e]], # ㅡ

    [[e, e],[e, e]], # ㅁ

    [[0, e],[e, e],[e, 0]], # ㄹ
    [[e, 0],[e, e],[0, e]],
    [[0, e, e],[e, e, 0]],
    [[e, e, 0],[0, e, e]],

    [[0, e, 0],[e, e, e]], # ㅏ
    [[e, e, e],[0, e, 0]],
    [[0, e],[e, e],[0, e]],
    [[e, 0],[e, e],[e, 0]],

    [[e, 0], [e, 0],[e, e]], # ㄱ
    [[e, e], [e, 0],[e, 0]],
    [[e, e], [0, e],[0, e]],
    [[0, e], [0, e],[e, e]],
    [[e, e, e], [e, 0, 0]],
    [[e, e, e], [0, 0, e]],
    [[e, 0, 0], [e, e, e]],
    [[0, 0, e], [e, e, e]],
]

def masking(a, b):
    return sum([a[i][j]&b[i][j] for i in range(len(a)) for j in range(len(a[0]))])

area=0
for i in range(N):
    for j in range(M):
        for block in blocks:
            r, c = len(block), len(block[0])
            if i+r<=N and j+c<=M:
                mask=[board[i][j:j+c] for i in range(i, i+r)]
                masked=masking(mask, block)
                area=max(masked, area)
print(area)
