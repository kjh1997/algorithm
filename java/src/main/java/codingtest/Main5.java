package codingtest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main5 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Set<String> data = new HashSet<>();
        for (int i = 0; i < n; i++) {
            data.add(br.readLine());
        }
        ArrayList<String> ans2 = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String tmp = br.readLine();
            if (data.contains(tmp)) {
                ans2.add(tmp);

            }
        }
        Collections.sort(ans2);
        System.out.println(ans2.size());
        for (String s : ans2
        ) {
            System.out.println(s);
        }
    }
}
