package Dproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class TimeInvocationHandler implements InvocationHandler {
    private final Object target;


    public TimeInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("Proxy start");
        long start = System.currentTimeMillis();
        Object result = method.invoke(target, args);
        long endtime = System.currentTimeMillis();
        long resultTime = endtime - start;
        System.out.println("Proxy 종료 result = " + resultTime);
        return result;
    }
}
