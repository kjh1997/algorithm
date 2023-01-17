package test2;

public class Battle {
    public static void main(String[] args) {
        Fighter f1 = new Fighter("Lew", 10, 2);
        Fighter f2 = new Fighter("Harry", 5, 4);
        fight(f1, f2, "Lew");
    }
    public static void fight(Fighter a, Fighter b, String name) {
        if (a.getName() == name) {
            extracted(b, a);
        } else {
            extracted(a, b);
        }
    }
    private static void extracted(Fighter a, Fighter b) {
        while (true) {
            if (a.underAttack(b)) {
                break;
            }
            if (b.underAttack(a)) {
                break;
            }
        }
    }
}
