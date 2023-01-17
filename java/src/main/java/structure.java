import java.util.*;

public class structure {
    public static void main(String[] args) {
        arrayList();

    }
    public static void priorityQueue() {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        heap.add(10);
        heap.add(100);
        heap.add(150);
        heap.add(120);
        heap.add(110);
        heap.add(50);
        heap.add(220);
        heap.add(130);
        heap.add(80);
        System.out.println(heap);
        System.out.println(heap.poll());
        System.out.println(heap.poll());
        System.out.println(heap.poll());
    }
    public static void stack() {
        Stack<String> str = new Stack<>();
    }

    public static void linkedList() {
        LinkedList<String> link = new LinkedList<>();
    }

    public static void intArray() {
        int[][] arr = new int[5][5];

    }
    public static void queue() {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            q.add(i);
        }
        System.out.println(q);
        System.out.println(q.peek());
        System.out.println(q.poll());
        System.out.println(q.poll());
    }
    public static void hashMap() {
        HashMap<String, String> strMap = new HashMap<>();
        strMap.put("test", "data");
        System.out.println(strMap.containsKey("test"));
        System.out.println(strMap.get("test"));
        strMap.replace("test", "update");
        System.out.println(strMap.get("test2"));

    }

    public static void set() {
        Set<String> set = new HashSet<>();
    }

    public static void arrayList() {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            arr.add(i);
        }
        ArrayList<Integer> arr2 = new ArrayList<>(arr.subList(0, 5));
        System.out.println(arr2.getClass());

        System.out.println(new ArrayList<Integer>(arr2).getClass());


    }




}
