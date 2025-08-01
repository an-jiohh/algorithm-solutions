package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Q1949 {
    static Map<Integer, List<Integer>> graph;
    static int[] city;
    static int[][] dp;
    static boolean[] visited;

    static void dfs(int node){
        dp[node][1] = city[node];
        for(int next:graph.get(node)){
            if(!visited[next]){
                visited[next] = true;
                dfs(next);
                dp[node][1] += dp[next][0];
                dp[node][0] += Math.max(dp[next][1], dp[next][0]);
            }
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] index = br.readLine().split(" ");
        city = new int[n+1];
        graph = new HashMap<>();
        dp = new int[n+1][2];
        visited = new boolean[n+1];
        for(int i = 1; i < index.length+1; i++){
            city[i] = Integer.parseInt(index[i-1]);
            graph.put(i, new ArrayList<>());
        }
        for(int i = 0; i < n-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        visited[1] = true;
        dfs(1);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }
}
