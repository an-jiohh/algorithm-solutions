package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Q2533 {
    static int[][] dp;
    static Map<Integer,List<Integer>> graph = new HashMap<>();
    static boolean[] visited;

    static void dfs(int node){
        dp[node][0] = 1;
        for(int child:graph.get(node)){
            if(!visited[child]){
                visited[child] = true;
                dfs(child);
                dp[node][0] += Math.min(dp[child][1], dp[child][0]); 
                dp[node][1] += dp[child][0];
            }
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        dp = new int[n+1][2]; // dp[node][0]: 얼리, dp[node][1]: 일반
        for(int i = 1; i < n+1; i++) graph.put(i, new ArrayList<>());
        for(int i = 0; i < n-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        visited = new boolean[n+1];
        visited[1] = true;
        dfs(1);
        System.out.println(Math.min(dp[1][0],dp[1][1]));
    }
}
