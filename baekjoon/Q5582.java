package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q5582 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        int n = a.length();
        int m = b.length();

        int[][] dp = new int[n+1][m+1];
        int answer = 0;
        for(int i = 1; i < n+1; i++){
            for(int j = 1; j < m+1; j++){
                if (a.charAt(i-1) == b.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if(dp[i][j] > answer) answer = dp[i][j];
                }
            }
        }
        System.out.println(answer);
    }
}
