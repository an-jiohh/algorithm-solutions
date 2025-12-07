package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Q11724 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int n = Integer.parseInt(index[0]);
        int m = Integer.parseInt(index[1]);

        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int i = 1; i <= n; i++) graph.put(i, new ArrayList<>());
        for(int i = 0; i < m; i++) {
            index = br.readLine().split(" ");
            int a = Integer.parseInt(index[0]);
            int b = Integer.parseInt(index[1]);
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new LinkedList<>();
        int answer = 0;
        for(int i = 1; i <= n; i++){
            if(!visited[i]){
                visited[i] = true;
                queue.add(i);
                while (!queue.isEmpty()) {
                    Integer now = queue.poll();
                    for(int next:graph.get(now)){
                        if(!visited[next]){
                            visited[next] = true;
                            queue.add(next);
                        }
                    }
                }
                answer++;
            }
        }
        System.out.println(answer);
    }
}
