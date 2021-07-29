package _02_거리두기;

import java.util.*;

class Point{
    int x;
    int y;
    int dist;
    boolean part;
    boolean person;
    public Point(int x, int y,int dist){
        this.x=x;
        this.y=y;
        this.dist=dist;
        this.part=false;
        this.person=false;
    }
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("{")
          .append("x : ").append(""+x).append(", ")
          .append("y : ").append(""+y).append(", ")
          .append("dist :").append(""+dist).append(", ")
          .append("part : ").append(""+part).append(", ")
          .append("person : ").append(""+person)
          .append("}");
        return sb.toString();
    }
}

class Solution {
    
    int dx[] = {0,1,0,-1};
    int dy[] = {-1,0,1,0};
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        int idx=0;
        
        for(String place[]:places){
            boolean flag=true;
            loop : for(int i=0;i<5;i++){
                for(int j=0;j<5;j++){
                    char c = place[i].charAt(j);
                    if(c!='P')
                        continue;
                    boolean visited[][]=new boolean[5][5];
                    LinkedList<Point> queue = new LinkedList<>();
                    queue.offer(new Point(j,i,0));
                    
                    while(!queue.isEmpty()){
                        Point p = queue.poll();
                        if((p.dist==1 && p.person) ||
                           (p.dist==2 && !p.part && p.person))
                        {
                            flag=false;
                            break loop;
                        }
                        if(p.dist==3)
                            break;
                        if(visited[p.y][p.x])
                            continue;
                        visited[p.y][p.x]=true;
                        
                        for(int k=0;k<4;k++){
                            
                            int nx = p.x+dx[k];
                            int ny = p.y+dy[k];
                            int dist = p.dist+1;
                            
                            boolean part = p.part;
                            if(nx>=0 && ny>=0 && nx<5 && ny<5 && !visited[ny][nx]){
                                Point p1 = new Point(nx,ny,dist);
                                p1.part=part;
                                if(place[ny].charAt(nx)=='X'){
                                    p1.part=true;
                                }else if(place[ny].charAt(nx)=='P'){
                                    p1.person=true;
                                }
                                queue.offer(p1);
                            }
                            
                        }
                        
                    }
                    
                    
                }
            }
            if(flag)
                answer[idx++]=1;
            else
                answer[idx++]=0;
        }
        
        return answer;
    }
}
