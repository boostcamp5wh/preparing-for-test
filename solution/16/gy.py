from bisect import bisect_left

def solution(infos, queries):
    MAX_CLASS = 4*3*3*3
    item_names = [
        ['cpp', 'java', 'python', '-'],
        ['backend', 'frontend', '-'],
        ['junior', 'senior', '-'],
        ['chicken', 'pizza', '-'],
    ]
    
    def get_class_idx(language, job, career, soulfood):
        return language * 27 + job * 9 + career * 3 + soulfood
    
    def get_all_class_idx(language, job, career, soulfood):
        for lan in [language, 3]:
            for jb in [job, 2]:
                for cr in [career, 2]:
                    for sf in [soulfood, 2]:
                        yield lan * 27 + jb * 9 + cr * 3 + sf
    
    
    applicants_by_class = [[] for _ in range(MAX_CLASS)] 
    for info in infos:
        tmp = info.split()
        score = int(tmp[-1])
        cur_items = [name.index(item) for name, item in zip(item_names, tmp[:-1])]
        for class_idx in get_all_class_idx(*cur_items):
            applicants_by_class[class_idx].append(score) 
    
    for applicants in applicants_by_class:
        applicants.sort()
    
    
    answer = []
    for query in queries:
        tmp = [x for x in query.split() if x != 'and']
        score = int(tmp[-1])
        cur_items = [name.index(item) for name, item in zip(item_names, tmp[:-1])]
        class_index = get_class_idx(*cur_items)
        answer.append(len(applicants_by_class[class_index]) - bisect_left(applicants_by_class[class_index], score))
    
    return answer
