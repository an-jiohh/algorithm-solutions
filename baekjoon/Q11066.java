package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q11066 {
    static int[][] dp;
    static int[] cost;
    static int[] preSum;
    public static int dfs(int start, int end) {
        if(start == end) return 0;

        if(dp[start][end] != 0) return dp[start][end];

        int temp = Integer.MAX_VALUE;

        for(int i = start; i < end; i++){
            temp = Integer.min(temp, dfs(start, i) + dfs(i+1,end) +preSum[end+1]-preSum[start]);
        }
        dp[start][end] = temp;
        return temp;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++){
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            cost = new int[n];
            preSum = new int[n+1];
            dp = new int[n][n];
            for(int i = 0; i < n; i++){
                cost[i] = Integer.parseInt(st.nextToken());
            }
            for(int i = 1; i < n+1; i++){
                preSum[i] = preSum[i-1] + cost[i-1];
            }
            System.out.println(dfs(0, n-1)); 
        }
    }
}
