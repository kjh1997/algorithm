package Interface;

public class People extends Parent implements Animal, Address {
    private String name;
    private String address;

    public People(String name, String address) {
        this.name = name;
        this.address = address;
    }

    @Override
    public String myhome() {
        return this.address;
    }

    @Override
    public void cry() {
        System.out.println("안녕하세요");
    }

    @Override
    public String myname() {
        System.out.println(test + test2);

        return this.name;
    }

}
