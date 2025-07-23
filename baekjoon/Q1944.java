package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q1944 {
    static int[] parents = null;
    static class Node{
        Node(int y, int x){
            this.x = x;
            this.y = y;
        }
        Node(int y, int x, int cost){
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
        public int y;
        public int x;
        public int cost;
    }
    static class Edge{ // a -> b
        public int a;
        public int b;
        public int cost;
        Edge(int a, int b, int cost){
            this.a = a;
            this.b = b;
            this.cost = cost;
        }
    }
    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String[] map = new String[n];
        for(int i = 0; i < n; i++){
            map[i] = br.readLine();
        }
        
        List<Node> nodes = new ArrayList<>();
        Map<String, Integer> node_num = new HashMap<>();

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(map[i].charAt(j) == 'K' || map[i].charAt(j) == 'S'){
                    node_num.put(String.valueOf(i)+","+String.valueOf(j), nodes.size());
                    nodes.add(new Node(i,j,0));
                }
            }
        }

        int[] nextX = {0,1,0,-1};
        int[] nextY = {1,0,-1,0};
        List<Edge> graph = new ArrayList<>();
        for(int i = 0; i < nodes.size(); i++){
            Queue<Node> queue = new LinkedList<>();
            boolean[][] visited = new boolean[n][n];
            Node start = nodes.get(i);
            queue.add(start);
            visited[start.y][start.x] = true;
            while (!queue.isEmpty()) {
                Node next = queue.poll();
                for(int j = 0; j < 4; j++){
                    int y = next.y + nextY[j];
                    int x = next.x + nextX[j];
                    if (0 <= y && y < n && 0 <= x && x < n && !visited[y][x] && map[y].charAt(x) != '1'){
                        visited[y][x] = true;
                        queue.add(new Node(y, x, next.cost +1));
                        if (node_num.containsKey(String.valueOf(y)+","+String.valueOf(x))){
                            int end = node_num.get(String.valueOf(y)+","+String.valueOf(x));
                            graph.add(new Edge(i, end, next.cost + 1));
                        }
                    }

                }
            }
        }
        parents = new int[nodes.size()];
        for(int i = 0; i < nodes.size(); i++){
            parents[i] = i;
        }

        graph.sort((a,b)-> Integer.compare(a.cost, b.cost));
        int answer = 0;
        int count = 0;
        for(int i = 0; i < graph.size(); i++){
            Edge e = graph.get(i);
            if(find(e.a) != find(e.b)){
                union(e.a, e.b);
                answer += e.cost;
                count += 1;
                if (count == nodes.size()-1){
                    break;
                }
            }
        }
        if(count != nodes.size()-1) answer = -1;
        System.out.println(answer);
    }

    public static int find(int x){
        if (parents[x] != x) {
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }
    public static void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY){
            parents[rootY] = rootX;
        }
    }
}
