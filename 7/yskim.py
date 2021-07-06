import sys
n=int(sys.stdin.readline())
students = (tuple(map(int, sys.stdin.readline().split())) for _ in range(n*n))
students = {i[0]:set(i[1:]) for i in students}
config = [[401*(not j%(n+1)) for j in range(n+2)] if i%(n+1) else [401]*(n+2) for i in range(n+2)]
def friend(student, r, c):
    global config, students
    return int(10**(sum(config[rn][cn] in students[student] for rn in range(r-1, r+2) for cn in range(c-1,c+2) if (rn-r+cn-c+2)%2)-1))
def blank(student, r, c):
    global config, students
    return sum(True for rn in range(r-1, r+2) for cn in range(c-1,c+2) if ((rn-r+cn-c+2)%2) and not config[rn][cn])
for student in students:
    m=0
    cond1={}
    for i in range(1,n+1):
        for j in range(1,n+1):    
            if config[i][j]==0 and m<=friend(student,i,j):
                if m<friend(student,i,j):
                    cond1={}
                cond1[i]=cond1.get(i,set())|{j}
                m=friend(student,i,j)
    m=0
    cond2={}
    for i in cond1:
        for j in cond1[i]:
            if m<=blank(student,i,j):
                if m<blank(student,i,j):
                    cond2={}
                cond2[i]=cond2.get(i,set())|{j}
                m=blank(student,i,j)
    r=min(cond2.keys())
    c=min(cond2[r])
    config[r][c]=student
print(sum(friend(config[i][j],i,j) for i in range(1,n+1) for j in range(1,n+1)))
