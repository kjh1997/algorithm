package Dproxy;

//import static sun.net.www.protocol.http.AuthCacheValue.Type.Proxy;

import java.lang.reflect.Proxy;

public class Main {

    public static void main(String[] args) {

        Cat cat = new Kitty();
        TimeInvocationHandler handler = getTimeInvocationHandler(cat);

        Cat proxy = getProxy(handler);

        proxy.call();


    }

    private static TimeInvocationHandler getTimeInvocationHandler(Cat cat) {
        TimeInvocationHandler handler = new TimeInvocationHandler(cat);
        return handler;
    }


    private static Cat getProxy(TimeInvocationHandler handler) {
        Cat proxy = (Cat) Proxy.newProxyInstance(Cat.class.getClassLoader(),
                new Class[]{Cat.class}, handler);
        return proxy;
    }
}
