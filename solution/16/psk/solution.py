from collections import defaultdict

def solution(info, query):
    answer = []
    m = defaultdict(list)
    
    lang=["cpp","java","python"]
    job=["backend","frontend"]
    career=["junior","senior"]
    soul=["chicken","pizza"]
        
    for i in lang:
        for j in job:
             for k in career:
                    for l in soul:
                        m[(i,j,k,l)]=list()
                        
    for ele in info:
        tmp=ele.split(" ")
        
        key=(tmp[0],tmp[1],tmp[2],tmp[3])
        arr=m[key]
        arr.append(int(tmp[4]))
        arr.sort()
        
        
                 
    for q in query:
        tmp=q.split(" ")
        score=int(tmp[7])
        a=[];b=[];c=[];d=[]
        if tmp[0]=='-':
            a=lang
        else:
            a=[tmp[0]]
        if tmp[2]=='-':
            b=job
        else:
            b=[tmp[2]]
        if tmp[4]=='-':
            c=career
        else:
            c=[tmp[4]]
        if tmp[6]=='-':
            d=soul
        else:
            d=[tmp[6]]
        cnt=0
        for i in a:
            for j in b:
                for k in c:
                    for l in d:
                        key=(i,j,k,l)
                        t=m[key]
                        left=0;right=len(t)-1;mid=0
                        while left<=right:
                            mid=(left+right)//2
                            if(t[mid]>=score):
                                right=mid-1
                            else:
                                left=mid+1
                        cnt+=len(t)-right-1
        answer.append(cnt)

    return answer