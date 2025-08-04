package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Q13334 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        for(int i = 0; i < n; i++){
            String[] index = br.readLine().split(" ");
            int a = Integer.parseInt(index[0]);
            int b = Integer.parseInt(index[1]);
            if (a > b) {arr[i][0] = b; arr[i][1] = a;}
            else {arr[i][0] = a; arr[i][1] = b;}
        }
        Arrays.sort(arr, (a,b)-> Integer.compare(a[1], b[1]));
        int l = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        int answer = 0;
        for(int i = 0; i < n; i++){
            int next_h = arr[i][0];
            int next_o = arr[i][1];
            if (next_o - next_h > l) continue;
            while(!queue.isEmpty() && queue.peek() < next_o - l){
                queue.poll();
            }
            queue.add(next_h);
            answer = Math.max(answer, queue.size());
        }
        System.out.println(answer);
    }
}