package cglib;

import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

import java.lang.reflect.Method;

public class MethodInterceptorImpl implements MethodInterceptor {

    @Override
    public Object intercept(Object object, Method method, Object[] args, MethodProxy methodProxy) throws Throwable {
        // TODO Auto-generated method stub
        System.out.println("before target Proxy");
        Object returnValue = methodProxy.invokeSuper(object, args);
        System.out.println("after target Proxy");
        return returnValue;
    }
}
