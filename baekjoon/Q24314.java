package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q24314 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int a1 = Integer.parseInt(index[0]);
        int b1 = Integer.parseInt(index[1]);
        int c = Integer.parseInt(br.readLine());
        int n0 = Integer.parseInt(br.readLine());
        boolean answer = false;
        if(a1 >= c && a1 * n0 + b1 >= c*n0) System.out.println(1);
        else System.out.println(0);
    }
}
