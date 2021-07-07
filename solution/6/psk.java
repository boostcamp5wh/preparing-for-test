package BOJ.implementation.컨베이어벨트위의로봇;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {

	
	static int n,k,answer=1;//answer는 곧 멈추는 단계를 말한다.
	static ArrayList<Integer> dura;
	static LinkedList<Boolean> conv;
	
	static void rotate() {
		conv.addFirst(conv.pollLast());
		dura.add(0,dura.remove(dura.size()-1));
		conv.set(n-1, false);
	}
	
	static void move() {
		for (int i = n - 2; i >= 0; i--) {
	        if ((!conv.get(i + 1)) && (dura.get(i + 1) > 0) && (conv.get(i))) {
	            conv.set(i, false);
	            conv.set(i+1,true);
	            dura.set(i+1, dura.get(i+1)-1);
	        }
	    }
	    
	    conv.set(n-1, false);
	}
	
	static void put_robot()
	{
		if(!conv.get(0) && dura.get(0)>0) {
			conv.set(0, true);
			dura.set(0, dura.get(0)-1);
		}
	}
	
	static int check()
	{
	    int cnt = 0;
	    for (int i = 0; i < 2 * n; i++) {
	        if (dura.get(i) == 0)
	            cnt++;
	    }
	    return cnt;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		n = Integer.parseInt(input[0]);
		k = Integer.parseInt(input[1]);
		
		input=br.readLine().split(" ");
		
		dura = new ArrayList<>(); //내구도
		conv = new LinkedList<>(); //컨베이어
		
		

		for(int i=0;i<2*n;i++) {
			dura.add(Integer.parseInt(input[i]));
			conv.add(false);
		}
		
		while (true) {
	        rotate();
	        move();
	        put_robot();

	        int c = check();
	        if (c >= k) {
	            System.out.println(answer);
	            br.close();
	            return ;
	        }
	        answer++;
	    }
		
//		br.close();
	}

}
