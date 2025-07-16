package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q1309 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] check = new int[3];
        check[0] = 1;check[1] = 1;check[2] = 1;
        for(int i = 1; i<n; i++){
            int check0 = (check[0] + check[1]  + check[2]) % 9901;
            int check1 = (check[0] + check[2])  % 9901;
            int check2 = (check[0] + check[1])  % 9901;
            check[0] = check0; check[1] = check1; check[2] = check2;
        }
        System.out.println((check[0] + check[1]  + check[2]) % 9901);
    }
}
