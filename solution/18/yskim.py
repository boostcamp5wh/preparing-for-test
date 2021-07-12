from collections import deque
def times(t):
    return sum(val*(60**(2-idx)) for idx, val in enumerate(map(lambda x:int(x), t.split(':'))))
def times_rev(t, string = ''):
    for i in range(2):
        string += str(f'{(t//(60**(2-i))):02d}:')
        t = t%(60**(2-i))
    return string+str(f'{t:02d}')
def solution(play_time, adv_time, logs, answer={}):
    def find(l, score, f=0):
        while f<=l:
            m = (f+l)//2
            if logs_dict['timeline'][m]>=score:
                l=m-1
            else:
                f=m+1
        return f
    play_time, adv_time = times(play_time), times(adv_time)
    logs_dict = {'timeline':{0,play_time-adv_time}, 0:0, play_time-adv_time:0}
    for log in logs:
        plus, minus = map(times, log.split('-'))
        logs_dict[plus], logs_dict[minus] = 1, -1
        logs_dict['timeline'].update((plus,minus))
    logs_dict['timeline'] = deque(sorted(logs_dict['timeline']))
    idx, mans, maxi = 0, 0, (0,0)
    while logs_dict['timeline']:
        time = logs_dict['timeline'].popleft()
        idx += 1
        mans += logs_dict[time]
        if logs_dict[time] != -1:
            l = find(len(logs_dict['timeline'])-1, time+adv_time)
            acc, cur_m, cur_t = 0, mans, time
            for i in range(l):
                acc, cur_t, cur_m = acc + cur_m*(logs_dict['timeline'][i]-cur_t), logs_dict['timeline'][i], cur_m + logs_dict[logs_dict['timeline'][i]]
            acc += cur_m*(time+adv_time-cur_t)
            if maxi[0] < acc:
                maxi = (acc,time)
    return times_rev(maxi[1])
