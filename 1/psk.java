package psk.baekjoon.atm;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static int atm_wait[];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		
		String s[] = sc.nextLine().split(" ");
		atm_wait = new int[n];
		
		for(int i=0;i<s.length;i++) {
			atm_wait[i]  = Integer.parseInt(s[i]);
		}
		
		Arrays.sort(atm_wait);
		int sum=0;
		
		for(int i=0;i<n;i++) {
			int people=0;
			for(int j=0;j<=i;j++) {
				people+=atm_wait[j];
			}
			sum+=people;
		}
		
		System.out.println(sum);
		
		sc.close();
		
	}


}
