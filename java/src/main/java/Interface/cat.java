package Interface;

public class cat implements Animal {


    public cat(String name) {
        this.name = name;
    }

    @Override
    public void cry() {
        System.out.println("cat");

    }

    private String name;
    @Override
    public String myname() {
        return name;
    }
}
