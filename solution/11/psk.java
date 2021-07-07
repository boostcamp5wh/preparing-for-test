package BOJ.bfs.연구소;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Dot {
	int x;
	int y;

	public Dot(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {

	static int lab[][];
	static int tempLab[][];
	static int n, m;
	static int ans = 0;

	static int dx[] = { 0, 0, -1, 1 };
	static int dy[] = { -1, 1, 0, 0 };

	static Queue<Dot> virus = new LinkedList<>();

//지도 복사
	static void mapCopy(int a[][], int b[][]) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				a[i][j] = b[i][j];
			}
		}
	}

//바이러스 퍼트리기(BFS)
	static void virusSpread() {
		// SpreadLab은 3개의 벽으로 막은 후 바이러스가 퍼졌을 때의 연구소의 상황을 저장하는곳.
		int SpreadLab[][] = new int[n][m];
		mapCopy(SpreadLab, tempLab);
		Queue<Dot> q = new LinkedList<>(virus);

		while (!q.isEmpty()) {
			Dot d = q.poll();
			int x = d.x;
			int y = d.y;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				// 연구소 범위 안에 감염되지 않은 영역만 오염시킬 수 있다.
				if (0 <= nx && nx < m && 0 <= ny && ny < n) {
					if (SpreadLab[ny][nx] == 0) {
						SpreadLab[ny][nx] = 2;
						q.offer(new Dot(nx, ny));
					}
				}
			}
		}
		// 연구소에 오염되지 않은 부분 체크.
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (SpreadLab[i][j] == 0)
					cnt += 1;
			}
		}
		ans = Math.max(ans, cnt);
	}

//벽 세우기(재귀호출 사용)
	static void wall(int cnt) {
		// 3개의 벽이 세워졌을 때, 바이러스를 퍼트린다.
		if (cnt == 3) {
			virusSpread();
			return;
		}
		// 벽 세우는 부분.
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (tempLab[i][j] == 0) {
					tempLab[i][j] = 1;
					wall(cnt + 1);
					// 모든 경우의 수를 넣어야하므로 기존의 1을 0으로 바꾸어주는 역활
					tempLab[i][j] = 0;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		lab = new int[n][m];
		tempLab = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				lab[i][j] = sc.nextInt();
				if (lab[i][j] == 2) {
					virus.offer(new Dot(j, i));
				}
			}
		}
		// 연구소에서 0인 부분을 모두 벽을 세워야 하므로 다음과 같이 진행.
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (lab[i][j] == 0) {
					mapCopy(tempLab, lab);
					tempLab[i][j] = 1;
					wall(1);
					tempLab[i][j] = 0;
				}
			}
		}
		System.out.printf("%d\n", ans);
		sc.close();
	}
}
