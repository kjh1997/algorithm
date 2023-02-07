package designpattern.factory.entity;

import designpattern.factory.Ship;

public class WhiteShip extends Ship {
    public WhiteShip() {
        setColor("white");
        setLogo("WhiteLogo");
        setName("WhiteShip");
    }
}
