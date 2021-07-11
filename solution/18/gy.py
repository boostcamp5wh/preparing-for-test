from functools import reduce
from collections import deque

def str2int(s):
    return reduce(lambda v, e: v*60+e, map(int, s.split(':')))

def int2str(n):
    sec = n % 60
    min = (n//60)%60
    hour = n//3600
    return f'{hour:02}:{min:02}:{sec:02}'

def interval2int(s):
    return list(map(str2int, s.split('-')))

def solution(play_time, adv_time, logs):
    play_num = str2int(play_time)
    adv_num = str2int(adv_time)
    logs_num = [interval2int(x) for x in logs]

    flatten_logs = []
    for log_start, log_end in logs_num:
        flatten_logs.append((log_start, 1))
        flatten_logs.append((log_end, -1))
    flatten_logs.sort()

    count_logs = []
    before_bef = 0
    bef, bef_type = flatten_logs[0]
    count = bef_type
    wall = 0
    for t, w in flatten_logs[1:] + [(-1, -1)]:
        if t != bef:
            if count != 0:
                count_logs.append((bef-before_bef, wall))
                wall += count

                count = 0
                before_bef = bef

        bef = t
        count += w

    # print('count_logs')
    # print(count_logs)
    
    count_logs.reverse()
    delta_time, _ = count_logs.pop()
    count_logs_len = len(count_logs)

    best = 0
    cur_time = 0
    answer_time = 0
    total = 0
    sliding_window = deque([(adv_num, 0)])

    while count_logs_len > 0:
        sw_count, sw_value = sliding_window[0]
        cl_count, cl_value = count_logs[-1]

        diff = min(sw_count, cl_count)
        cur_time += diff
        total += (cl_value - sw_value) * diff\

        if total > best:
            best = total
            answer_time = cur_time

        sliding_window.append([diff, cl_value])

        sw_count -= diff
        if sw_count == 0:
            sliding_window.popleft()
        else:
            sliding_window[0] = (sw_count, sw_value)
        

        cl_count -= diff
        if cl_count == 0:
            count_logs.pop()
            count_logs_len -= 1
        else:
            count_logs[-1] = (cl_count, cl_value)

    answer_time = delta_time + answer_time - adv_num
    if answer_time < 0:
        answer_time = 0
    answer = int2str(answer_time)
    return answer
