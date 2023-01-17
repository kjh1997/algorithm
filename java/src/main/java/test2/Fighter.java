package test2;

public class Fighter {
    private String name;
    private int health;
    private int damegePerAttack;


    public Fighter(String name, int health, int damegePerAttack) {
        this.name = name;
        this.health = health;
        this.damegePerAttack = damegePerAttack;
    }

    public String getName() {
        return name;
    }
    public boolean underAttack(Fighter fighter) {

        System.out.println(fighter.name + " attacks " + name + ";" + name + " now has " + (health - fighter.damegePerAttack));
        health -= fighter.damegePerAttack;
        if (health <= 0) {
            System.out.println("dead." + fighter.name + " wins");
            return true;
        }
        return false;

    }


}
