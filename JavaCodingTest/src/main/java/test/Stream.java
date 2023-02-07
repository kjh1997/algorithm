package test;

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntBinaryOperator;
import java.util.stream.Collectors;

public class Stream {
    public static void main(String[] args) {


        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < 10; i++) {

            arr.add(i);
        }
        List<Integer> collect = arr.stream()
                .collect(Collectors.filtering(i -> i % 4 == 0, Collectors.toList()));
        System.out.println(collect);
        arr.forEach(System.out::println);




    }

}
