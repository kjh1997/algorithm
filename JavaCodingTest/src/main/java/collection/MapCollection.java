package collection;

import java.util.HashMap;
import java.util.Map;

public class MapCollection {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("kjh", "kind");
        map.put("kjy", "sub");
        map.put("kjm", "stupid");
        map.put("test", "123");
        map.forEach((k, v) -> System.out.println(k + " | " + v));
        map.forEach((k,v) -> {
            if (v.length() > 3) {
                System.out.println(k + " | " + v);
            }});


    }
}
