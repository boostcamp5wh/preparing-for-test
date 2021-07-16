def solution(s):
    words = 'zero one two three four five six seven eight nine'
    alpha2num = {w[:2]: (n, len(w)) for w, n in zip(words.split(), range(10))}
    
    answer = 0
    idx = 0
    while idx < len(s):
        if '0' <= s[idx] <= '9':
            num = int(s[idx])
            skip_idx = 1
        else:
            num, skip_idx = alpha2num[s[idx:idx+2]]
            
        answer = 10 * answer + num
        idx += skip_idx
            
    return answer
