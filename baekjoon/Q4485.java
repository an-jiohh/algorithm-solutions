package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q4485 {
    static class Node {
        int y;
        int x;
        int cost;
        Node(int y, int x, int cost){
            this.y = y;
            this.x = x;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = 0;
        while (true) {
            count += 1;
            int n = Integer.parseInt(br.readLine());
            if(n == 0) break;
            int[][] value = new int[n][n];
            int[][] dist = new int[n][n];
            for(int i = 0; i < n; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j = 0; j < n; j++){
                    value[i][j] = Integer.parseInt(st.nextToken());
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
            int[] moveY = {0,0,-1,1};
            int[] moveX = {1,-1,0,0};
            PriorityQueue<Node> queue = new PriorityQueue<>((a,b)->Integer.compare(a.cost, b.cost));
            queue.add(new Node(0, 0, value[0][0]));
            dist[0][0] = value[0][0];
            while(!queue.isEmpty()){
                Node now = queue.poll();
                if(dist[now.y][now.x] < now.cost) continue;
                for(int i = 0; i < 4; i++){
                    int my = now.y + moveY[i];
                    int mx = now.x + moveX[i];
                    if(0 <= my && my < n && 0<= mx && mx < n){
                        if(dist[my][mx] > now.cost + value[my][mx]){
                            dist[my][mx] = now.cost + value[my][mx];
                            queue.add(new Node(my, mx, now.cost + value[my][mx]));
                        }
                    }
                }
            }
            System.out.println("Problem "+count+": "+dist[n-1][n-1]);
        }
    }
}
