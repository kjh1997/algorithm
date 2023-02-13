package cglib;

public class PersonService {
    public String sayHello(String name) {
        System.out.println("Hello" +name);
        return "Hello" +name;
    }

    public Integer lengthOfName(String name) {
        return name.length();
    }
}
