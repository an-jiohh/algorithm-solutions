package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q9370 {
    public static Map<Integer, List<Edge>> graph = new HashMap<>();
    static class Edge {
        int node;
        long cost;
        Edge(int node, long cost){
            this.node = node;
            this.cost = cost;
        }
        
    }
    public static long[] deikstra(int start, int n){
        long[] dist = new long[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        PriorityQueue<Edge> queue = new PriorityQueue<>((a,b) -> Long.compare(a.cost, b.cost));
        queue.add(new Edge(start, 0));
        dist[start] = 0;
        while (!queue.isEmpty()) {
            Edge now = queue.poll();
            if(dist[now.node] < now.cost) continue;
            for(Edge nextEdge:graph.get(now.node)){
                if(dist[nextEdge.node] > now.cost + nextEdge.cost){
                    dist[nextEdge.node] = now.cost + nextEdge.cost;
                    queue.add(new Edge(nextEdge.node, now.cost + nextEdge.cost));
                }
            }
        }
        return dist;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for(int test = 0; test < testCase; test++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int h  = Integer.parseInt(st.nextToken());
            for(int i = 1; i < n+1; i++) graph.put(i, new ArrayList<>());
            long ghSize = 0;
            for(int i = 0; i < m; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int d  = Integer.parseInt(st.nextToken());
                graph.get(a).add(new Edge(b, d));
                graph.get(b).add(new Edge(a, d));
                if((a == g && b == h) || (a == h && b == g)){
                    ghSize = d;
                }
            }
            List<Integer> target = new ArrayList<>();
            for(int i = 0; i < t; i++){
                int temp = Integer.parseInt(br.readLine());
                target.add(temp);
            }
            long[] startS = deikstra(s, n);
            long[] startG = deikstra(g, n);
            long[] startH = deikstra(h, n);
            List<Integer> answers = new ArrayList<>();            
            for (int x : target) {
                long SGHX = startS[g] + ghSize + startH[x];
                long SHGX = startS[h] + ghSize + startG[x];
                if(SGHX == startS[x] || SHGX == startS[x]){
                    answers.add(x);
                }
            }
            answers.sort((a,b) -> Integer.compare(a, b));
            StringBuilder sb = new StringBuilder();
            for (Integer answer : answers) {
                sb.append(String.valueOf(answer + " "));
            }
            System.out.print(sb);
        }
    }
}
