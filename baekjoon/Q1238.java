package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Q1238 {
    static class Edge {
        int node;
        int cost;
        Edge(int node, int cost){
            this.node = node;
            this.cost = cost;
        }
    }
    static Map<Integer, List<Edge>> graph = new HashMap<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int n = Integer.parseInt(index[0]);
        int m = Integer.parseInt(index[1]);
        int x = Integer.parseInt(index[2]);
        for(int i = 0; i < n+1; i++) graph.put(i, new ArrayList<>());
        for(int i = 0; i < m; i++) {
            index = br.readLine().split(" ");
            int a = Integer.parseInt(index[0]);
            int b = Integer.parseInt(index[1]);
            int c = Integer.parseInt(index[2]);
            graph.get(a).add(new Edge(b, c));
        }
        List<int[]> dijikList = new ArrayList<>();
        dijikList.add(new int[n+1]);
        for(int i = 1; i < n+1; i++){
            dijikList.add(dijkstra(n, i));
        }
        int answer = Integer.MIN_VALUE;
        for(int i = 1; i < n+1; i++){
            answer = Math.max(answer, dijikList.get(i)[x] + dijikList.get(x)[i]);
        }
        System.out.println(answer);
    }

    public static int[] dijkstra(int n, int s){
        int[] dist = new int[n+1];
        for(int i = 0; i < n+1; i++) dist[i] = Integer.MAX_VALUE;
        PriorityQueue<Edge> queue = new PriorityQueue<>((a,b) -> Integer.compare(a.cost, b.cost));
        queue.add(new Edge(s, 0));
        dist[s] = 0;
        while (!queue.isEmpty()) {
            Edge now = queue.poll();
            if(dist[now.node] < now.cost) continue;
            for(Edge next:graph.get(now.node)){
                if(dist[next.node] > now.cost + next.cost){
                    dist[next.node] = now.cost + next.cost;
                    queue.add(new Edge(next.node, now.cost + next.cost));
                }
            }
        }
        return dist;
    }
}
