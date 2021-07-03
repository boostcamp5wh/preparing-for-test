from collections import defaultdict

n = int(input())
max_student = n**2

students = [list(map(int, input().split())) for _ in range(max_student)]

classroom = [[-1] * n for _ in range(n)]

def nearby(y, x, n):
	dy = [0, 0, -1, 1]
	dx = [-1, 1, 0, 0]
	for i in range(4):
		new_y = y + dy[i]
		new_x = x + dx[i]
		if 0 <= new_y < n and 0 <= new_x < n:
			yield new_y, new_x

nearby_empty = [[4] * n for _ in range(n)]
for i in range(n):
	nearby_empty[i][0] -= 1
	nearby_empty[i][-1] -= 1
	nearby_empty[0][i] -= 1
	nearby_empty[-1][i] -= 1

students_sat_locations = {}
for student in students:

	most_liked_seats = []
	most_liked_cnt = 0
	like_nearby_cnts = defaultdict(int)

	for like_student in student[1:]:
		if like_student in students_sat_locations:
			y, x = students_sat_locations[like_student]
			for n_y, n_x in nearby(y, x, n):
				if classroom[n_y][n_x] != -1:
					continue

				like_nearby_cnts[(n_y, n_x)] += 1
				if like_nearby_cnts[(n_y, n_x)] > most_liked_cnt:
					most_liked_seats = [(n_y, n_x)]
					most_liked_cnt += 1
				elif like_nearby_cnts[(n_y, n_x)] == most_liked_cnt:
					most_liked_seats.append((n_y, n_x))

	if most_liked_cnt == 0:
		next_seat = (0, 0)
		best_empty = nearby_empty[0][0]
		for i in range(n):
			for j in range(n):
				if nearby_empty[i][j] > best_empty:
					best_empty = nearby_empty[i][j]
					next_seat = (i, j)
	else:
		next_seat = min(most_liked_seats, key=lambda x: (-nearby_empty[x[0]][x[1]], x[0], x[1]))

	nearby_empty[next_seat[0]][next_seat[1]] = -1
	classroom[next_seat[0]][next_seat[1]] = student[0]
	students_sat_locations[student[0]] = next_seat

	for n_y, n_x in nearby(next_seat[0], next_seat[1], n):
		nearby_empty[n_y][n_x] -= 1

score = 0
score_table = [0, 1, 10, 100, 1000]
for student in students:
	student_pos = students_sat_locations[student[0]]
	liked_cnt = 0
	for n_y, n_x in nearby(student_pos[0], student_pos[1], n):
		if classroom[n_y][n_x] in student[1:]:
			liked_cnt += 1
	score += score_table[liked_cnt]

print(score)	
