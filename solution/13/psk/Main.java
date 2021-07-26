package BOJ.implementation.톱니바퀴;

import java.io.BufferedReader;
import java.io.InputStreamReader;

// 참고 : https://bcp0109.tistory.com/33
public class Main {
    // 톱니바퀴 [번호][방향]
    static int[][] arr = new int[4][8];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int i = 0; i < 4; i++) {
            String s = br.readLine();
            for (int j = 0; j < 8; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }

        int k = Integer.parseInt(br.readLine());

        // 톱니바퀴 회전
        for (int i = 0; i < k; i++) {
            String input[]=br.readLine().split(" ");
            int idx = Integer.parseInt(input[0]);
            int dir = Integer.parseInt(input[1]);

            // 톱니바퀴 번호는 1~4, 인덱스는 0~3
            solution(idx - 1, dir);
        }

        // 점수 계산
        int score = 0;
        for (int i = 0; i < 4; i++) {
            score += arr[i][0] * (1 << i);
        }

        System.out.println(score);
        br.close();
    }

    // 9시 방향은 2, 3시 방향은 6
    static void solution(int idx, int dir) {
        left(idx - 1, -dir);
        right(idx + 1, -dir);
        rotate(idx, dir);
    }

    // 왼쪽에 있던 톱니바퀴 회전 여부 결정
    static void left(int idx, int dir) {
        if (idx < 0) return;

        if (arr[idx][2] != arr[idx + 1][6]) {
            left(idx - 1, -dir);
            rotate(idx, dir);
        }
    }

    // 오른쪽에 있던 톱니바퀴 회전 여부 결정
    static void right(int idx, int dir) {
        if (idx > 3) return;

        if (arr[idx][6] != arr[idx - 1][2]) {
            right(idx + 1, -dir);
            rotate(idx, dir);
        }
    }

    // dir = 1 시계방향, dir = -1 반시계방향
    static void rotate(int idx, int dir) {
        if (dir == 1) {
            int temp = arr[idx][7];

            for (int i = 7; i > 0; i--) {
                arr[idx][i] = arr[idx][i - 1];
            }

            arr[idx][0] = temp;

        } else {
            int temp = arr[idx][0];

            for (int i = 0; i < 7; i++) {
                arr[idx][i] = arr[idx][i + 1];
            }

            arr[idx][7] = temp;
        }
    }
}
