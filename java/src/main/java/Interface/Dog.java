package Interface;

public class Dog implements Animal {

    public Dog(String name) {
        this.name = name;
    }

    @Override
    public void cry() {
        System.out.println("dog");

    }

    private String name;
    @Override
    public String myname() {
        return this.name;
    }
}
