package BOJ.implementation.테트로미노;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input[]=br.readLine().split(" ");
		
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		
		int arr[][]= new int[n][];
		
		for(int i=0;i<n;i++) {
			input = br.readLine().split(" ");
			int[] tmp = new int[m];
			for(int j=0;j<input.length;j++) {
				tmp[j] = Integer.parseInt(input[j]);
			}
			arr[i] = tmp;
		}
		int max = 1;
		for(int i=0;i<n-1;i++)
			for(int j=0;j<m-1;j++)
			{
				int x = j;
				int y = i;
				int sum = arr[y][x] + arr[y+1][x]+arr[y][x+1]+arr[y+1][x+1];
				
				max = Math.max(max, sum);
			}
		
		for(int i=0;i<n;i++)
			for(int j=0;j<m-3;j++)
			{
				int x = j;
				int y = i;
				int sum = arr[y][x] + arr[y][x+1]+arr[y][x+2]+arr[y][x+3];
				
				max = Math.max(max, sum);
			}
		
		for(int i=0;i<n-3;i++)
			for(int j=0;j<m;j++)
			{
				int x = j;
				int y = i;
				int sum = arr[y][x] + arr[y+1][x]+arr[y+2][x]+arr[y+3][x];
				
				max = Math.max(max, sum);
			}
		
		for(int i=0;i<=n-3;i++)
			for(int j=0;j<=m-2;j++) {
				int x = j;
				int y = i;
				
				int line_sum=0;
				for(int k=0;k<3;k++) {
					line_sum+=arr[y+k][x];
				}
				for(int k=0;k<3;k++) {
					max = Math.max(line_sum+arr[y+k][x+1], max);
				}
				line_sum=0;
				for(int k=0;k<3;k++) {
					line_sum+=arr[y+k][x+1];
				}
				for(int k=0;k<3;k++) {
					max = Math.max(line_sum+arr[y+k][x], max);
				}
				line_sum = arr[y][x]+arr[y+1][x]+arr[y+1][x+1]+arr[y+2][x+1];
				max = Math.max(line_sum, max);
				line_sum = arr[y][x+1]+arr[y+1][x+1]+arr[y+1][x]+arr[y+2][x];
				max = Math.max(line_sum, max);
			}
		
		for(int i=0;i<=n-2;i++)
			for(int j=0;j<=m-3;j++) {
				int x = j;
				int y = i;
				
				int line_sum=0;
				for(int k=0;k<3;k++) {
					line_sum+=arr[y][x+k];
				}
				for(int k=0;k<3;k++) {
					max = Math.max(line_sum+arr[y+1][x+k], max);
				}
				line_sum=0;
				for(int k=0;k<3;k++) {
					line_sum+=arr[y+1][x+k];
				}
				for(int k=0;k<3;k++) {
					max = Math.max(line_sum+arr[y][x+k], max);
				}
				line_sum = arr[y][x]+arr[y][x+1]+arr[y+1][x+1]+arr[y+1][x+2];
				max = Math.max(line_sum, max);
				line_sum = arr[y+1][x]+arr[y+1][x+1]+arr[y][x+1]+arr[y][x+2];
				max = Math.max(line_sum, max);
			}
		System.out.println(max);
		br.close();
	}

}
