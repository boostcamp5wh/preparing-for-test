import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
mx = 2 * n
ar = list(map(int, input().split()))
robots = [False] * mx

up = 0
drop = n-1
zero_cnt = ar.count(0)
step = 0

get_before_index = lambda x: x-1 if x >= 0 else x+mx-1

while zero_cnt < k:
	step += 1


	up = get_before_index(up)
	drop =  get_before_index(drop)
	if robots[drop]:
		robots[drop] = False

	idx = drop
	while idx != up:
		before_idx = get_before_index(idx)
		if robots[before_idx] and not robots[idx] and ar[idx] >= 1:
			ar[idx] -= 1
			robots[idx] = True
			robots[before_idx] = False

			if idx == drop:
				robots[idx] = False
			if ar[idx] == 0:
				zero_cnt += 1

		idx = before_idx

	if ar[up] >= 1:
		ar[up] -= 1
		robots[up] = True
		if ar[idx] == 0:
			zero_cnt += 1

print(step)
