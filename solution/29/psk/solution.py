from collections import deque

def solution(places):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    answer = []
    
    for place in places:
        flag=True
        # print(idx)
        for i in range(5):
            loop1=False
            for j in range(5):
                c = place[i][j]
                if c!='P':
                    continue
                visited = [[False for _ in range(5)] for a in range(5)]
                # queue = deque([Point(j,i,0)])
                queue = deque([(j,i,0,False,False)])
                while queue:
                    # print(queue)
                    x,y,dist,part,person = queue.popleft()
                    # x,y,dist,part,person
                    if (dist==2 and not part and person) or (dist==1 and person):
                        flag=False
                        break
                    if dist==3:
                        break
                    if visited[y][x]:
                        continue
                    visited[y][x]=True;
                    for k in range(4): 
                        nx = x+dx[k]
                        ny = y+dy[k]
                        # print(nx,ny)
                        n_dist = dist+1
                        n_part = part
                        # print(visited)
                        if (0<=nx<5) and (0<=ny<5) and visited[ny][nx]==False:
                            # print('들어오는 가',nx,ny)
                            p_part=n_part;
                            p_person = False
                            if place[ny][nx]=='X':
                                p_part=True
                            elif place[ny][nx]=='P':
                                p_person=True
                            queue.append((nx,ny,n_dist,p_part,p_person))
                if not flag:
                    loop1=True
                    break
            if loop1:
                break             
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer