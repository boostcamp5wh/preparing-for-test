package kakaoBlind2021._06_카드짝맞추기;

import java.util.*;

class Point{
    int x,y;
    Point(int x,int y){
        this.x=x;
        this.y=y;
    }
}

class Solution {
    
    static int dx[]={1,-1,0,0};
    static int dy[]={0,0,1,-1};
    
    static int p[]=new int[6];
    static boolean isused[]=new boolean[7];
    static int n=0;
    static int answer = Integer.MAX_VALUE;
    static Point occur[][]=new Point[7][2];
    static int[][] bboard = new int[4][4];
    static int row,col;
    
    public int solution(int[][] board, int r, int c) {
        row = r; col = c;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                bboard[i][j] = board[i][j];
        for(int i = 0; i < 7; i++){
            occur[i][0] = new Point(-1, -1);
            occur[i][1] = new Point(-1, -1);      
        }
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(board[i][j] == 0) 
                    continue;
                if(occur[board[i][j]][0].x == -1){
                    occur[board[i][j]][0] = new Point(i, j);
                    n++;
                }
                else
                    occur[board[i][j]][1] = new Point(i, j);
            }
        }
        solve(0);
        return answer + 2*n;
    }
    
    // BFS
    static int dist(int[][] board, Point s, Point e){
        //s : 시작점, e : 끝점
        
        int d[][]=new int[4][4];
        for(int i=0;i<4;i++)
            Arrays.fill(d[i],-1);
        
        d[s.x][s.y]=0;
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(s.x,s.y));
        while(!queue.isEmpty()){
            Point cur = queue.poll();
            for(int i=0;i<4;i++){
                
                int dis=0;
                //해당 방향으로 진행할 때 카드 혹은 마지막 칸까지의 거리
                
                while(true){
                    int nx = cur.x+dx[i]*dis;
                    int ny = cur.y+dy[i]*dis;
                    if(nx+dx[i]<0 || nx+dx[i]>3 || 
                      ny+dy[i]<0 || ny+dy[i]>3
                      || (dis!=0 && board[nx][ny]!=0) )
                        break;
                    dis++;
                }
                
                for(int j = 0; j < 2; j++){
                    int z = 1;
                    if(j == 1) 
                        z = dis;
                    int nx = cur.x + dx[i] * z;
                    int ny = cur.y + dy[i] * z;
                    if(nx<0 || nx>3 || ny<0 || ny>3) 
                        continue;
                    if(d[nx][ny] == -1){
                        d[nx][ny] = d[cur.x][cur.y] + 1;
                        queue.add(new Point(nx, ny));
                    }
                }
                
            }
        }
        return d[e.x][e.y];
    }
    
    static void solve(int idx){
        if(idx == n){ 
            // p[0], p[1], ... , p[n-1]에 permutation을 채움
            int myboard[][] = new int[4][4];
            for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                    myboard[i][j] = bboard[i][j];
            int d[][] = new int[6][2];
            
            d[0][0] = dist(myboard, new Point(row, col), occur[p[0]][0]) + dist(myboard, occur[p[0]][0], occur[p[0]][1]);
            d[0][1] = dist(myboard, new Point(row, col), occur[p[0]][1]) + dist(myboard, occur[p[0]][1], occur[p[0]][0]);
            myboard[occur[p[0]][0].x][occur[p[0]][0].y] = 0;
            myboard[occur[p[0]][1].x][occur[p[0]][1].y] = 0;
            for(int i = 1; i < n; i++){
                d[i][0] = Math.min(d[i-1][0] + dist(myboard, occur[p[i-1]][1], occur[p[i]][0]), d[i-1][1] + dist(myboard, occur[p[i-1]][0], occur[p[i]][0])) + dist(myboard, occur[p[i]][0], occur[p[i]][1]);
                d[i][1] = Math.min(d[i-1][0] + dist(myboard, occur[p[i-1]][1], occur[p[i]][1]), d[i-1][1] + dist(myboard, occur[p[i-1]][0], occur[p[i]][1])) + dist(myboard, occur[p[i]][1], occur[p[i]][0]);
                myboard[occur[p[i]][0].x][occur[p[i]][0].y] = 0;
                myboard[occur[p[i]][1].x][occur[p[i]][1].y] = 0;    
            }
            answer = Math.min(Math.min(answer, d[n-1][0]), d[n-1][1]);
        }
        for(int i = 1; i <= 6; i++){
            if(occur[i][0].x == -1 || isused[i]) 
                continue;
            p[idx] = i;
            isused[i] = true;
            solve(idx+1);
            isused[i] = false;            
        }
    }
}
