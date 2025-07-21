package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q1958 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        String c = br.readLine();
        int n = a.length();
        int m = b.length();
        int l = c.length();
        int[][][] dp = new int[n+1][m+1][l+1];
        for(int i = 1; i < n+1; i++){
            for(int j = 1; j < m+1; j++){
                for(int k = 1; k < l+1; k++){
                    if (a.charAt(i-1) == b.charAt(j-1) && b.charAt(j-1) == c.charAt(k-1)){
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
                    } else {
                        int[] temp = {dp[i-1][j][k], dp[i][j-1][k],dp[i][j][k-1]};
                        dp[i][j][k] = Arrays.stream(temp).max().getAsInt();
                    }
                }
            }
        }
        System.out.println(dp[n][m][l]);
    }
}
