package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q14621 {
    static List<Edge> graph = new ArrayList<>();
    static int[] parents;

    public static class Edge {
        int start;
        int end;
        int cost;
        Edge(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
    }

    public static int find(int x) {
        if(parents[x] != x){
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }

    public static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parents[rootY] = rootX;
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int n = Integer.parseInt(index[0]);
        int m = Integer.parseInt(index[1]);
        String[] sex = br.readLine().split(" ");
        parents = new int[n];
        for(int i = 0; i < n; i++) parents[i] = i;
        for(int i =0; i < m; i++){
            String[] uvd = br.readLine().split(" ");
            int u = Integer.parseInt(uvd[0]) - 1;
            int v = Integer.parseInt(uvd[1]) - 1;
            int d = Integer.parseInt(uvd[2]);
            if(!sex[u].equals(sex[v])) {
                graph.add(new Edge(u, v, d));
            }
        }
        int count = 0;
        int answer = 0;
        graph.sort((a,b) -> Integer.compare(a.cost, b.cost));
        for(Edge edge:graph){
            if(find(edge.start) != find(edge.end)){
                union(edge.start, edge.end);
                count++;
                answer += edge.cost;
                if(count == n-1) break;
            }
        }
        if(count != n-1) answer = -1;
        System.out.println(answer);
    }
}
