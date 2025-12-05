package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Q1325 {
    public static Map<Integer, List<Integer>> graph = new HashMap<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] index = br.readLine().split(" ");
        int n = Integer.parseInt(index[0]), m = Integer.parseInt(index[1]);
        for(int i = 1; i <= n; i++) graph.put(i, new ArrayList<>());
        for(int i = 0; i < m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(b).add(a);
        }
        int[] answers = new int[n+1];
        for(int i = 1; i <= n; i++){
            boolean[] visited = new boolean[n+1];
            visited[i] = true;
            Queue<Integer> queue = new LinkedList<>();
            queue.add(i);
            int count = 0;
            while(!queue.isEmpty()){
                int now = queue.poll();
                for(int next:graph.get(now)){
                    if(!visited[next]){
                        visited[next] = true;
                        queue.add(next);
                        count++;
                    }
                }
            }
            answers[i] = count;
        }
        int max = Arrays.stream(answers).max().getAsInt();
        StringBuffer sb = new StringBuffer();
        for(int i = 1; i <= n; i++){
            if(answers[i] == max) {
                sb.append(i);
                sb.append(" ");
            }
        }
        System.out.println(sb);
    }
}
