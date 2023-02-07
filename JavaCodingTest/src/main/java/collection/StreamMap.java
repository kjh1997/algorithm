package collection;

import java.util.ArrayList;

public class StreamMap {
    public static void main(String[] args) {
        ArrayList<String> arr = new ArrayList<>();
        arr.add("kjh123");
        arr.add("kjy123");
        arr.add("kjm123");
        arr.add("kjh4325");
        arr.stream().map(String::length).peek(
                i->
                {
                    if (i < 10) {
                        System.out.println("min : " + i );
                    }
                }

                ).map(i -> i * i).peek(i -> {
            if (i >= 30) {
                System.out.println("test.test : " + i);
            }
        }).forEach(System.out::println);
    }
}
