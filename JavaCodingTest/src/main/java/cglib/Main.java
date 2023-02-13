package cglib;

import designpattern.Test;
import net.sf.cglib.proxy.*;

import java.lang.reflect.Method;

public class Main {
    public static void main(String[] args) throws Exception {
        CglibEx2();
    }




    public static void CglibEx2() {
        Enhancer enhancer = new Enhancer();
        enhancer.setSuperclass(PersonService.class);
        enhancer.setCallback(new MethodInterceptorImpl());
        Object target = enhancer.create();
        System.out.println(System.identityHashCode(target) + " | " + target.getClass());
        PersonService personService = (PersonService) target;
        personService.sayHello(" kjh");

    }


}
