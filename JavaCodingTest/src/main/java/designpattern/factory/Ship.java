package designpattern.factory;

import lombok.Data;

@Data
public class Ship {

    private String name;
    private String color;
    private String logo;

    public String getName() {
        return name;
    }


    @Override
    public String toString() {
        return "Ship { " +
                "name = '" + name + '\''+
                ", color = '" + name + '\''+
                ", logo = '" + name + '\'' +
                "}";
    }


}
