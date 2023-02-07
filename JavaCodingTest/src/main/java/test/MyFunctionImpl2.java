package test;

public class MyFunctionImpl2 implements MyFunction {

    @Override
    public int max(int a, int b) {
        System.out.println("testestet");;
        return a > b ? a * a : b * b;
    }
}
