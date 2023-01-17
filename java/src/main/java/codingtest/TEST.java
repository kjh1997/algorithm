package codingtest;

import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class TEST {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int arr[];
    static StringTokenizer st ;
    static int n, m;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        Arrays.sort(arr);
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (bSearch(num)) {
                bw.write("1 ");
            } else {
                bw.write("0 ");
            }
        }
        bw.close();
        br.close();
    }

    public static Boolean bSearch(int target) {
        int s = 0;
        int e = arr.length -1 ;
        while (s <= e) {
            int mid = (s + e) / 2;
            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                s = mid +1;
            } else {
                e = mid -1;
            }
        }
        return false;
    }


}
