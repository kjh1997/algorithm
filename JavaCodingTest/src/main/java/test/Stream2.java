package test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Stream2 {
    public static void main(String[] args) {
        Map<Integer,Integer> arr = new HashMap<>();
        for (int i =0; i<10;i++){
            arr.put(i, i);
        }
        arr.forEach((k,v)->System.out.println(k+v));

        ArrayList<Integer> arrInt = new ArrayList<>();
        for (int i =0; i<10;i++){
            arrInt.add(i);

        }
        arrInt.stream().filter(i->i%2==0).forEach(System.out::println);



    }
}
