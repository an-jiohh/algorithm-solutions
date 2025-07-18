package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q9252 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        int n = a.length();
        int m = b.length();
        String[][] dp = new String[n+1][m+1];
        for(int i = 0; i < n+1; i++){
            for(int j = 0; j < m+1; j++){
                dp[i][j] = "";
            }
        }
        for(int i = 1; i < n+1; i++){
            for(int j = 1; j < m+1; j++){
                if (a.charAt(i-1) == b.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] + a.charAt(i-1);
                } else {
                    if (dp[i-1][j].length() > dp[i][j-1].length()) {
                        dp[i][j] = dp[i-1][j];
                    } else {
                        dp[i][j] = dp[i][j-1];
                    }
                }
            }
        }
        System.out.println(dp[n][m].length());
        System.out.println(dp[n][m]);
    }
}