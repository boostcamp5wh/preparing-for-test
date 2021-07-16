package BOJ.implementation.로봇청소기;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	static int n;
	static int m;
	static final int NORTH = 0;
	static final int SOUTH = 2;
	static final int EAST = 1;
	static final int WEST = 3;
	static int answer=0;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String input[]=br.readLine().split(" ");
		n = Integer.parseInt(input[0]);
		m = Integer.parseInt(input[1]);
		input = br.readLine().split(" ");
		int r = Integer.parseInt(input[0]);
		int c = Integer.parseInt(input[1]);
		int d = Integer.parseInt(input[2]);
		
		int map[][]=new int[n][m];
		
		for(int i=0;i<n;i++) {
			input = br.readLine().split(" ");
			for(int j=0;j<m;j++)
				map[i][j] = Integer.parseInt(input[j]);
		}
		
		//0 : 북쪽, 1 : 동쪽, 2: 남쪽, 3 : 서쪽
		whileloop: while(r >=0 && c >=0 && r < n && c < m) {
			map[r][c]=-1; // 현재 위치를 청소
			forloop : for(int i=0;i<=4;i++) {
				
				if(i==4) {
					switch(d) {
					case EAST->{
						if(map[r][c-1]==1) {
							break whileloop;
						}
						c--;
					}
					case WEST->{
						if(map[r][c+1]==1) {
							break whileloop;
						}
						c++;
					}
					case SOUTH->{
						if(map[r-1][c]==1) {
							break whileloop;
						}
						r--;
					}
					case NORTH->{
						if(map[r+1][c]==1) {
							break whileloop;
						}
						r++;
					}
				}
					continue;
				}
				
				switch(d) {
					case EAST->{
						d = NORTH;
						if(map[r-1][c]==0) {
							r--;
							break forloop;
						}else continue;
						
					}
					case WEST->{
						d = SOUTH;
						if(map[r+1][c]==0) {
							r++;
							break forloop;
						}else continue;
						
					}
					case SOUTH->{
						d = EAST;
						if(map[r][c+1]==0) {
							c++;
							break forloop;
						}else continue;
						
					}
					case NORTH->{
						d = WEST;
						if(map[r][c-1]==0) {
							c--;
							break forloop;
						}else continue;
						
					}
				}
			}
			
			
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
//				System.out.print(map[i][j] + "\t");
				if(map[i][j]==-1)
					answer++;
			}
//			System.out.println();
		}
			
				
		bw.write(answer+"\n");
		bw.close();
		br.close();
	}

}
