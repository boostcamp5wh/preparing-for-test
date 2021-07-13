def times(time):
    h, m, s = map(int, time.split(':'))
    return h*3600 + m*60 + s
def solution(play_time, adv_time, logs):
    play_time, adv_time = times(play_time), times(adv_time)
    mans = [0]*(play_time+1)
    for log in logs:
        enter, out = map(times, log.split('-'))
        mans[enter] += 1
        mans[out] -= 1
    for i in range(1,len(mans)):
        mans[i] += mans[i-1]
    max_v, max_t = sum(mans[:adv_time]), 0
    value = max_v
    for i in range(1,play_time+1-adv_time):
        value += mans[adv_time+i-1] - mans[i-1]
        if value > max_v:
            max_v, max_t = value, i
    return f'{max_t//3600:02}:{(max_t%3600)//60:02}:{max_t%60:02}'
