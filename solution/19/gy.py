def solution(s):
    def count2len(n):
        if n <= 1:
            return 0
        if n < 10:
            return 1
        if n < 100:
            return 2
        return 3
    
    len_s = len(s)
    answer = len_s
    for pat_len in range(1, len_s // 2 + 1):
        total = len_s % pat_len
        count = 1
        pat_begin = 0
        for i in range(pat_len, len_s-total, pat_len):
            is_same = True
            for j in range(pat_len):
                if s[pat_begin+j] != s[i+j]:
                    is_same = False
                    break
            
            if is_same:
                count += 1
            else:
                total += count2len(count) + pat_len
                count = 1
                pat_begin = i
                
        total += count2len(count) + pat_len
        
        answer = min(answer, total)
    
    return answer
