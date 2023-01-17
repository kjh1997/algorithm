package Interface;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main7 {
    static BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    static int[] dx = {0, 0, 1, -1, -1, 1, -1, 1};
    static int[] dy = {1, -1, 0, 0, 1, 1, -1, -1};
    static int[][] arr;
    static boolean[][] visit;
    static int w,h;

    public static void main(String[] args) throws IOException {
        while (true) {
            StringTokenizer st = new StringTokenizer(bufferedReader.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0) {
                return;
            }
            arr= new int[h][w];
            visit = new boolean[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(bufferedReader.readLine());
                for (int j = 0; j < w; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (!visit[i][j] && arr[i][j] == 1) {
                        ans++;
                        cal(i, j);
                    }
                }
            }
            System.out.println(ans);

        }


    }

    private static void cal(int dh, int dw) {
        visit[dh][dw] = true;
        for (int i = 0; i < 8; i++) {
            int cx = dw + dx[i];
            int cy = dh + dy[i];

            if (0 <= cx && cx < w && 0 <= cy && cy < h && !visit[cy][cx] && arr[cy][cx] == 1) {
                cal(cy, cx);
            }
        }
    }


}
