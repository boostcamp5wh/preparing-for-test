package psk.baekjoon.���谨��;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String tmp[] = br.readLine().split(" ");
		
		
		String[] tmp1 = br.readLine().split(" ");
		int b = Integer.parseInt(tmp1[0]);
		int c = Integer.parseInt(tmp1[1]);

		int answer=n;
		for(int i=0;i<tmp.length;i++) {
			int t=Integer.parseInt(tmp[i]); //����� ��
			
			t=t-b>=0?t-b:0;
			if(t%c==0) {
				answer+=(t/c);
			}else {
				answer+=(t/c)+1;
			}
			
		}
		System.out.println(answer);
		br.close();
	}

}
