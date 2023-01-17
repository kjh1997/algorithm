package codingtest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main1697 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] visit = new int[100001];

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());
        Queue<Integer> q = new LinkedList<>();
        visit[n] = 1;
        q.add(n);
        while (!q.isEmpty()) {
            int tmp = q.poll();

            if (tmp == target) {
                System.out.println(visit[target]-1);
                return;
            }
            if (tmp * 2 <= 100000 && visit[tmp * 2] == 0) {
                q.add(tmp * 2);
                visit[tmp * 2] = visit[tmp] + 1;
            }
            if ( tmp - 1 >= 0 && visit[tmp - 1] == 0 ) {
                q.add(tmp - 1);
                visit[tmp-1] = visit[tmp] +1;
            }
            if (tmp + 1 <= 100000 && visit[tmp + 1] == 0) {
                q.add(tmp + 1);
                visit[tmp+1] = visit[tmp] +1;
            }
        }
    }
}
