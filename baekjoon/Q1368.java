package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q1368 {
    public static class Edge {
        int start;
        int next;
        int cost;

        Edge(int start, int next, int cost){
            this.start = start;
            this.next = next;
            this.cost = cost;
        }
    }
    static int[] parents;
    
    static int find(int x){
        if (parents[x] != x){
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }

    static void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if(rootX != rootY) {
            parents[rootY] = rootX;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Edge> graph = new ArrayList<>();
        for(int i = 1; i < n+1; i++){
            int cost = Integer.parseInt(br.readLine());
            graph.add(new Edge(0, i, cost));
        }
        for(int i = 1; i < n+1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 1; j < n+1; j++){
                int cost = Integer.parseInt(st.nextToken());
                if(i != j) graph.add(new Edge(i, j, cost));
            }
        }
        graph.sort((a, b) -> Integer.compare(a.cost, b.cost));
        parents = new int[n+1];
        for(int i = 0; i < n+1; i++) parents[i] = i;

        int answer = 0;
        int count = 0;
        for(Edge edge:graph){
            if(find(edge.start) != find(edge.next)){
                union(edge.start, edge.next);
                answer += edge.cost;
                count += 1;
                if (count == n) break;
            }
        }
        System.out.println(answer);
    }
}
