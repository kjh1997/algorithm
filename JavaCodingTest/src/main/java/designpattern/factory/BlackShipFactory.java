package designpattern.factory;

import designpattern.factory.entity.Blackship;

public class BlackShipFactory extends DefaultShipFactory {
    @Override
    public Ship createShip() {
        return new Blackship();
    }
}
