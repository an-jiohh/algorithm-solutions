package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q10844 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int mod = 1000000000;
        int n = Integer.parseInt(br.readLine());
        long[][] arr = new long[n][10];
        for(int i = 1; i < 10; i++){
            arr[0][i] = 1;
        }
        for(int i = 1; i < n; i++){
            arr[i][0] = arr[i-1][1];
            for(int j = 1; j < 9; j++){
                arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1]) % mod;
            }   
            arr[i][9] = arr[i-1][8];        
        }
        System.out.println(Arrays.stream(arr[n-1]).sum() % mod);
    }
}
