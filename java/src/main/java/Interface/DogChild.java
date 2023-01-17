package Interface;

public class DogChild extends Dog {
    private String name;
    private Integer age;

    public DogChild(String name) {
        super(name);
    }

    public void setter(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return this.name + " | " + this.age.toString();

    }
}
