package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q1562 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int MOD = 1_000_000_000;
        int BIT = 1 << 10; // 10000000000
        int[][][] dp = new int[n][10][BIT];

        for(int i = 1; i < 10; i++){
            dp[0][i][1 << i] = 1;
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j < 10; j++){
                for(int k = 0; k < BIT; k++){
                    int next = k | 1 << j;

                    if(0 < j) dp[i][j][next] += dp[i-1][j-1][k];
                    if(j < 9) dp[i][j][next] += dp[i-1][j+1][k];

                    dp[i][j][next] %= MOD;
                }
            }
        }
        int answer = 0;
        for(int i = 0; i < 10; i++){
            answer += dp[n-1][i][BIT-1];
            answer %= MOD;
        }
        System.out.println(answer);
    }
}
