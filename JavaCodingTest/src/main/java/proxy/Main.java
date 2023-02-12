import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<String> obj = new ArrayList<>();
        obj.add("test");
        Collection<String> obj2 = new ArrayList<>();
        obj2.add("?test");
        List<Object> obj3 = new ArrayList<>();
        obj3.add("test");
        int[] arr = new int[10];
        arr[0] = 5;
        arr[1] = 3;
        arr[7] = 6;
        System.out.println();
        try {
            throw new RuntimeException();

        } catch (IndexOutOfBoundsException e) {

            System.out.println("1" + e);
        } catch (RuntimeException e) {
            System.out.println("2" + e);
        }


        Arrays.sort(arr);
        System.out.println(System.identityHashCode(arr));

    }
}
