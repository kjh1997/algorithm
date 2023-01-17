package test;

public class FirstClass implements solve {


    @Override
    public int cal() {
        /*
        @filename 1번 문제 해결
         */
        int ans = 0;
        for (int i = 1; i < 11; i++) {
            ans += i;
        }
        return ans;
    }

}
