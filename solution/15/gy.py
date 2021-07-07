from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    orders = [sorted(list(order)) for order in orders]
        
    for course_len in course:
        ordered_cnt = defaultdict(int)
        max_courses = []
        max_cnt = 0
        for order in orders:
            for order_comb in combinations(order, course_len):
                course_name = ''.join(order_comb)
                ordered_cnt[course_name] += 1
                if ordered_cnt[course_name]  > max_cnt:
                    max_cnt = ordered_cnt[course_name] 
                    max_courses = [course_name]
                elif ordered_cnt[course_name]  == max_cnt:
                    max_courses.append(course_name)
        
        if max_cnt >= 2:
            answer.extend(max_courses)
    
    answer.sort()
    return answer
