package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q1753 {
    static class Edge {
        int node;
        int cost;
        Edge(int node, int cost){
            this.node = node;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int v = Integer.parseInt(index[0]);
        int e = Integer.parseInt(index[1]);
        Map<Integer, List<Edge>> graph = new HashMap<>();
        for(int i = 1; i < v+1; i++) graph.put(i, new ArrayList<>());

        int k = Integer.parseInt(br.readLine());
        for(int i = 0; i < e; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Edge(b, c));
        }
        
        PriorityQueue<Edge> queue = new PriorityQueue<>((a,b) -> Integer.compare(a.cost, b.cost));
        int[] dist = new int[v+1];
        for(int i = 0; i < v+1; i++) dist[i] = Integer.MAX_VALUE;
        dist[k] = 0;
        queue.add(new Edge(k, 0));
        while(!queue.isEmpty()){
            Edge now = queue.poll();
            if(dist[now.node] < now.cost){
                continue;
            }
            for(Edge next:graph.get(now.node)){
                if(dist[next.node] > now.cost + next.cost) {
                    dist[next.node] = now.cost + next.cost;
                    queue.add(new Edge(next.node, now.cost + next.cost));
                }
            }
        }
        for(int i = 1; i < v+1; i++){
            if(dist[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }
    }
}
