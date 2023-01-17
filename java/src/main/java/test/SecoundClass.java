package test;

public class SecoundClass implements solve {


    @Override
    public int cal() {
        int ans = 0;
        for (int i = 10; i < 21; i++) {
            if (i % 2 == 0) {
                ans ++;
            }
        }
        return ans;
    }

}
