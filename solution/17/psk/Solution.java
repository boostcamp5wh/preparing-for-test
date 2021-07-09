package kakaoBlind2021._04_гу╫бец╫ц©Д╠щ;

import java.util.*;
public class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        final int INF=1000000;
        int d[][]=new int[n][n];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                if(i!=j)
                    d[i][j]=INF;
        }

        for(int[] fare:fares){
            int p1=fare[0]-1;
            int p2=fare[1]-1;
            d[p2][p1]=d[p1][p2]=fare[2];
        }
        System.out.println(Arrays.deepToString(d));
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                for(int k=0;k<n;k++){
                    // if(d[j][k] > d[j][i] + d[i][k])
						d[j][k] = Math.min(d[j][i] + d[i][k],d[j][k]);
                }
        
        for(int k=0;k<n;k++)
            answer=Math.min(d[s-1][k]+d[k][a-1]+d[k][b-1],answer);
        return answer;
    }
}