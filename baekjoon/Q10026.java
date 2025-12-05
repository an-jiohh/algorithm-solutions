package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Q10026 {

    static class Node {
        int y;
        int x;
        Node(int y, int x){
            this.y = y;
            this.x = x;
        }
    }

    static public void bfs(String[][] pixel, boolean[][] visited, int y, int x, int n){
        int[] moveY = {0,0,-1,1};
        int[] moveX = {1,-1,0,0};

        Queue<Node> queue = new LinkedList<>();
        String color = pixel[y][x];
        queue.add(new Node(y,x));
        while(!queue.isEmpty()){
            Node start = queue.poll();
            for(int i = 0; i < 4; i++){
                int nextY = moveY[i] + start.y;
                int nextX = moveX[i] + start.x;
                if(0 <= nextX && nextX < n && 0 <= nextY && nextY < n){
                    if(!visited[nextY][nextX] && pixel[nextY][nextX].equals(color)){
                        visited[nextY][nextX] = true;
                        queue.add(new Node(nextY, nextX));
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        String[][] pixel = new String[num][];

        for(int i = 0; i < num; i++){
            pixel[i] = br.readLine().split("");
        }

        boolean[][] visited = new boolean[num][num];

        int answerBasic = 0;
        for(int i = 0; i < num; i++){
            for(int j = 0; j < num; j++){
                if(!visited[i][j]){
                    bfs(pixel, visited, i, j, num);
                    answerBasic++;
                }
            }
        }

        visited = new boolean[num][num];
        for(int i = 0; i < num; i++){
            for(int j = 0; j < num; j++){
                if(pixel[i][j].equals("G")) pixel[i][j] = "R";
            }
        }

        int answer = 0;
        for(int i = 0; i < num; i++){
            for(int j = 0; j < num; j++){
                if(!visited[i][j]){
                    bfs(pixel, visited, i, j, num);
                    answer++;
                }
            }
        }
        System.out.println(answerBasic + " " + answer);
    }
}
