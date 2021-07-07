package BOJ.dp.Επ»η;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				int n = Integer.parseInt(br.readLine());
				int t[] = new int[n+2];
				int p[]= t.clone();
				int d[] = t.clone();
				int result=0;
				for(int i=1; i<=n; i++){
		            String[] s = br.readLine().split(" ");
		            t[i] = Integer.parseInt(s[0]);
		            p[i] = Integer.parseInt(s[1]);
		        }
		  
		        for(int i=1; i<=n+1; i++){
		            for(int j=1; j<i; j++){
		                d[i] = Math.max(d[i], d[j]);
		                if(j + t[j] == i){
		                    d[i] = Math.max(d[i], d[j] + p[j]);
		                }
		            }

		            result = Math.max(result, d[i]);
		        }

		        System.out.println(result);
		        br.close();
				
	}

}