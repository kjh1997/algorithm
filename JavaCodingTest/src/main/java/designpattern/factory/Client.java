package designpattern.factory;

import designpattern.factory.entity.WhiteShip;
import jdk.swing.interop.SwingInterOpUtils;

public class Client {
    public static void main(String[] args) {
        /*
        구체적으로 어떤 인스턴스가 만들어지는 서브 클래스가 정한다.
        입력된 변수에 따라 인터페이스가 구현된 구현체가 달라진다.
         */

        Client client = new Client();
        client.print( "whiteship", "test01@gmail.com");
        client.print( "blackship", "test02@gmail.com");




    }

    private void print(String name, String email) {
        ShipFactory shipFactory = getShipFactory(name);
        System.out.println(shipFactory.orderShip(name, email));
    }

    private ShipFactory getShipFactory(String name) {
        ShipFactory shipFactory;
        if (name == "whiteship") {
            shipFactory = new WhiteShipFactory();
        } else if (name == "blackship") {
            shipFactory = new BlackShipFactory();
        } else {
            throw new IllegalArgumentException("선택한 선박이 없습니다.");
        }
        return shipFactory;
    }


}






