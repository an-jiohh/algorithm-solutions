package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Q1504 {
    static class Edge {
        int node;
        int cost;

        Edge(int node, int cost){
            this.node = node;
            this.cost = cost;
        }
    }
    static Map<Integer, List<Edge>> graph = new HashMap<>();

    static long deikstra(int start, int end, int n) {
        long[] dist = new long[n+1];
        for(int i = 0; i < n+1; i++) dist[i] = Integer.MAX_VALUE;
        dist[start] = 0;
        PriorityQueue<Edge> queue = new PriorityQueue<>((a,b) -> Integer.compare(a.cost, b.cost));
        queue.add(new Edge(start, 0));
        while (!queue.isEmpty()) {
            Edge now = queue.poll();
            if(dist[now.node] < now.cost) continue;
            for(Edge next:graph.get(now.node)){
                if(dist[next.node] > next.cost + now.cost){
                    dist[next.node] = next.cost + now.cost;
                    queue.add(new Edge(next.node, next.cost + now.cost));
                }
            }
        }
        return dist[end];
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int N = Integer.parseInt(index[0]);
        int E = Integer.parseInt(index[1]);
        for(int i = 1; i < N+1; i++) graph.put(i, new ArrayList<>());
        for(int i = 0; i < E; i++){
            index = br.readLine().split(" ");
            int a = Integer.parseInt(index[0]);
            int b = Integer.parseInt(index[1]);
            int c = Integer.parseInt(index[2]);
            graph.get(a).add(new Edge(b, c));
            graph.get(b).add(new Edge(a, c));
        }
        index = br.readLine().split(" ");
        int v1 = Integer.parseInt(index[0]);
        int v2 = Integer.parseInt(index[1]);
        long v1First = deikstra(1, v1, N) + deikstra(v1, v2, N) + deikstra(v2, N, N);
        long v2First = deikstra(1, v2, N) + deikstra(v2, v1, N) + deikstra(v1, N, N);
        long answer = Math.min(v1First, v2First);
        if(answer >= Integer.MAX_VALUE){
            answer = -1;
        }
        System.out.println(answer);
    }
}
