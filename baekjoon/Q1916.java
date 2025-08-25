package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q1916 {
    static class Edge {
        int end;
        int cost;
        Edge(int end, int cost){
            this.end = end;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        List<List<Edge>> graph = new ArrayList<>();
        for(int i = 0; i < n+1; i++) graph.add(new ArrayList<>());
        for(int i = 0; i < m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Edge(b, c));
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        PriorityQueue<Edge> queue = new PriorityQueue<>((a,b) -> {return Integer.compare(a.cost, b.cost);});
        int[] dist = new int[n+1];
        for(int i = 0; i < n+1; i++) dist[i] = Integer.MAX_VALUE;
        boolean[] visited = new boolean[n+1];
        queue.add(new Edge(start, 0));
        while(!queue.isEmpty()){
            Edge now = queue.poll();
            if(visited[now.end]){
                continue;
            }
            visited[now.end] = true;
            for(Edge next:graph.get(now.end)){
                if(dist[next.end] > now.cost + next.cost) {
                    dist[next.end] = now.cost + next.cost;
                    queue.add(new Edge(next.end, now.cost + next.cost));
                }
            }
        }
        System.out.println(dist[end]);
    }
}
