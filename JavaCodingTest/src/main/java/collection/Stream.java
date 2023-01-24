package collection;

import java.text.Collator;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Stream {
    public static void main(String[] args) {
        ArrayList<Long> arr = new ArrayList<>();
        for (long i =0; i < 1000000000; i++) {
            arr.add(i);
        }


        long beforeTime = System.currentTimeMillis();


        List<Long> arr3 = arr.parallelStream().collect(Collectors.filtering(i -> i % 2 == 0, Collectors.toList()));
        List<Long> arr2 = arr.stream().collect(Collectors.filtering(i -> i % 2 == 0, Collectors.toList()));

//        System.out.println(arr2);


        long afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
        long DiffTime = (afterTime - beforeTime) ; //두 시간에 차 계산
        System.out.println("시간차이(m) : " + DiffTime);
    }

}
