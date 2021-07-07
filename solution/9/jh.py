N, M, x, y, K = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(N)]
cmd=map(int, input().split())

class Dice:
    def __init__(self, init=[0, 0, 0, 0, 0, 0]):
        self.top=init[0]
        self.bottom=init[1]
        self.left=init[2]
        self.right=init[3]
        self.front=init[4]
        self.back=init[5]

    def roll(self, way):
        if way=='W': self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top
        elif way=='E': self.top, self.left, self.bottom, self.right = self.left, self.bottom, self.right, self.top
        elif way=='N': self.top, self.front, self.bottom, self.back = self.front, self.bottom, self.back, self.top
        elif way=='S': self.top, self.back, self.bottom, self.front = self.back, self.bottom, self.front, self.top
    
    def prt(self):
        print(self.top)

# dice=dice([1, 6, 4, 3, 5, 2])
dice=Dice()
D={1:'E', 2:'W', 3:'N', 4:'S'}

for i in cmd:
    if i==1 and y+1<M: y+=1        
    elif i==2 and y-1>-1: y-=1
    elif i==3 and x-1>-1: x-=1
    elif i==4 and x+1<N: x+=1
    else: continue

    dice.roll(D[i])
    if board[x][y]!=0:
        dice.bottom=board[x][y]
        board[x][y]=0
    else: board[x][y]=dice.bottom
    dice.prt()
