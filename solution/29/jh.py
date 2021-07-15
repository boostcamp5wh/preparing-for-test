def check(room):
    pos=[[r, c] for r in range(5) for c in range(5) if room[r][c]=='P']
    for i, a in enumerate(pos[:-1]):
        for b in pos[i+1:]:
            if b[0]-a[0]+abs(b[1]-a[1])<2: return False
            elif b[0]-a[0]+abs(b[1]-a[1])==2:
                if a[0]==b[0] and room[a[0]][a[1]+1]!='X': return False
                elif a[1]==b[1] and room[a[0]+1][a[1]]!='X': return False
                elif a[0]!=b[0] and a[1]!=b[1]:
                    if a[0]<4 and room[a[0]+1][a[1]]!='X': return False
                    if room[a[0]][b[1]]!='X': return False
    return True
    
def solution(places):
    return [1 if check(room) else 0 for room in places]
        
