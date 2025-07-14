package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Q10216 {

    private static int[] parent; 

    private static int find(int x){
        if (parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private static void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY){
            parent[rootY] = rootX;
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++){
            int n = Integer.parseInt(br.readLine());
            List<int[]> position = new ArrayList<>();
            parent = new int[n+1];
            for(int i = 0; i < n; i++){
                String[] nums = br.readLine().split(" ");
                position.add(new int[] {
                    Integer.parseInt(nums[0]),
                    Integer.parseInt(nums[1]),
                    Integer.parseInt(nums[2])});
                parent[i] = i;
            }
            for(int i = 0; i < n; i++){
                int startX = position.get(i)[0];
                int startY = position.get(i)[1];
                int startR = position.get(i)[2];
                for(int j = i+1; j < n; j++){
                    int nextX = position.get(j)[0];
                    int nextY = position.get(j)[1];
                    int nextR = position.get(j)[2];
                    if((int) Math.pow(startX-nextX, 2) + (int) Math.pow(startY-nextY, 2) <= (int) Math.pow(nextR+startR, 2)){
                        union(i,j);
                    }
                }
            }
            Set<Integer> answer = new HashSet<>();
            for(int i = 0; i < n; i++){
                answer.add(find(i));
            }
            System.out.println(answer.size());
        }
    }
}
