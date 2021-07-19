def solution(places, answer=[]):
    def safe(r, c, matrix):
        mp = {'O':0, 'P':1, 'X':-1}
        mat = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if (abs(2-i)+abs(2-j)<=2) and (0<=r-2+i<5) and (0<=c-2+j<5):
                    mat[i][j] = mp[matrix[r-2+i][c-2+j]]
        if mat[1][2]==1 or mat[2][1]==1 or mat[2][3]==1 or mat[3][2]==1:
            return 1
        if (mat[0][2]+mat[1][2])>0 or (mat[2][0]+mat[2][1])>0 or (mat[2][4]+mat[2][3])>0 or (mat[4][2]+mat[3][2])>0:
            return 1
        if (mat[1][1]==1 and mat[1][1]+mat[1][2]+mat[2][1]>-1) or (mat[1][3]==1 and  mat[1][3]+mat[1][2]+mat[2][3]>-1) or \
        (mat[3][1]==1 and  mat[3][1]+mat[2][1]+mat[3][2]>-1) or (mat[3][3]==1 and  mat[3][3]+mat[2][3]+mat[3][2]>-1):
            return 1
        return 0
    for place in places:
        breaking = 0
        for r, pla in enumerate(place):
            for c, p in enumerate(pla):
                if p=='P':
                    breaking = safe(r, c, place)
                if breaking:
                    break
            if breaking:
                break
        answer.append(1-breaking)
    return answer
