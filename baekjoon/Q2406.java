package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q2406 {

    static class Edge {
        int a;
        int b;
        int cost;
        Edge(int a, int b, int cost){
            this.a = a;
            this.b = b;
            this.cost = cost;
        }
    }

    static int find(int x){
        if(parents[x] != x){
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }

    static int union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if(rootX != rootY){
            parents[rootY] = rootX;
            return 1;
        }
        return 0;
    }

    public static int[] parents;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parents = new int[n+1];
        for(int i = 0; i < n; i++) parents[i] = i;

        int count = 0;
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            count += union(a, b);
        }

        int[][] cost = new int[n][n];
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                cost[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        List<Edge> graph = new ArrayList<>();
        for(int i = 1; i < n; i++){
            for(int j = i+1; j < n; j++){
                graph.add(new Edge(i+1, j+1, cost[i][j]));
            }
        }
        graph.sort((a,b)->(Integer.compare(a.cost, b.cost)));

        List<Edge> answerList = new ArrayList<>();
        int answer = 0;
        for(Edge target:graph){
            if(find(target.a) != find(target.b)){
                answerList.add(target);
                answer += target.cost;
                count += 1;
                union(target.a, target.b);
                if(count == n-2){
                    break;
                }
            }
        }
        StringBuffer sb = new StringBuffer();
        sb.append(answer + " " + answerList.size() + "\n");
        for(Edge answerNode:answerList){
            sb.append(answerNode.a);
            sb.append(" ");
            sb.append(answerNode.b);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
