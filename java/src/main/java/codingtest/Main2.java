package codingtest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] arr = {0,1,2,4,0,0,0,0,0,0,0,0,0,0};
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        for (int i = 1; i < 12; i++) {
            dp(i);
        }
        for (int i = 0; i < n; i++) {
            System.out.println(dp(Integer.parseInt(br.readLine())));

        }

    }

    public static int dp(int n) {
        if (arr[n] == 0) {
            arr[n] = dp(n - 1) + dp(n - 2) + dp(n - 3);
            return arr[n];
        }
        return arr[n];




    }
}
