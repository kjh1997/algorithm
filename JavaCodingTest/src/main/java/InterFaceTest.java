import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.lang.Math.max;

public class InterFaceTest {


    public static void main(String[] args) {
        MyFunction a = new MyFunctionImpl2();
        System.out.println(a.max(6,7));

        ArrayList<List<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            arr.add(new ArrayList<>());
        }
        System.out.println(arr);
        arr.get(2).get(2);
    }
}


