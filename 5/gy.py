n = int(input())
ar = list(map(int, input().split()))
op = list(map(int, input().split()))

op_funcs = [
	lambda x, y: x + y,
	lambda x, y: x - y,
	lambda x, y: x * y,
	lambda x, y: x // y if x > 0 else -((-x) // y),
]

def solve(idx, result, op_left):
	if idx == n-1:
		return result, result

	max_result = float('-inf')
	min_result = float('inf')
	for op_index, op_func in enumerate(op_funcs):
		if op_left[op_index] > 0:
			new_result = op_func(result, ar[idx+1])
			op_left[op_index] -= 1
			new_max_result, new_min_result = solve(idx+1, new_result, op_left)
			max_result = max(max_result, new_max_result)
			min_result = min(min_result, new_min_result)
			op_left[op_index] += 1
	return max_result, min_result

max_result, min_result = solve(0, ar[0], op)
print(max_result)
print(min_result)
