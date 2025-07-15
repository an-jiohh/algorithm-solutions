package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1520 {

    static int[][] visited;
    static int m;
    static int n;
    static int[] dirX = {0,-1,0,1};
    static int[] dirY = {1,0,-1,0};
    static int[][] map;

    static int dfs(int y,int x) {
        if (y == m-1 && x == n-1){
            visited[y][x] += 1;
            return 1;
        }
        if (visited[y][x] != -1){
            return visited[y][x];
        }
        int count = 0;
        for(int i = 0; i < 4; i++){
            int nextY = y + dirY[i];
            int nextX = x + dirX[i];
            if(0 <= nextY && nextY < m && 0 <= nextX && nextX < n){
                if(map[y][x] > map[nextY][nextX] ){
                    count += dfs(nextY, nextX);
                }
            }
        }
        visited[y][x] = count;
        return visited[y][x];
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        m = Integer.parseInt(index[0]);
        n = Integer.parseInt(index[1]);
        map = new int[m][n];
        visited = new int[m][n];
        for(int i = 0; i < m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = -1;
            }
        }
        dfs(0, 0);

        System.out.println(visited[0][0]);
    }
}
