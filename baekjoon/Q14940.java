package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q14940 {

    public static class Node {
        int value;
        int x;
        int y;
        Node(int x,int y,int value){
            this.x = x;
            this.y = y;
            this.value = value;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int n = Integer.valueOf(index[0]);
        int m = Integer.valueOf(index[1]);

        int[][] map = new int[n][m];
        int[][] answerMap = new int[n][m];
        int startX = 0, startY = 0;
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < m; j++){
                map[i][j] = Integer.valueOf(st.nextToken());
                if(map[i][j] == 2) {startX = j; startY = i;}
            }
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(startX,startY, 0));
        int[] dirX = {0,-1,0,1};
        int[] dirY = {1,0,-1,0};
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            for(int i = 0; i < 4; i++){
                int nextX = node.x + dirX[i];
                int nextY = node.y + dirY[i];
                if(0 <= nextX && nextX < m && 0<= nextY && nextY < n){
                    if(map[nextY][nextX] == 1 && answerMap[nextY][nextX] == 0){
                        answerMap[nextY][nextX] = node.value + 1;
                        queue.add(new Node(nextX, nextY, node.value+1));
                    }
                }
            }
        }
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if (startX == j && startY == i){
                    answerMap[i][j] = 0;
                } else if(map[i][j] == 0){
                    answerMap[i][j] = 0;
                } else if (answerMap[i][j] == 0){
                    answerMap[i][j] = -1;
                }
                answer.append(answerMap[i][j] + " ");  
            }
            answer.append("\n");
        }
        System.out.println(answer);
    }
}
