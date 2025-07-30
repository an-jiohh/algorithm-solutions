package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Q1655 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> left = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> right = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine());
        int center = Integer.parseInt(br.readLine());
        StringBuffer sb = new StringBuffer();
        sb.append(center + "\n");
        for(int i = 1; i < n; i++){
            int num = Integer.parseInt(br.readLine());
            if(num <= center) left.add(num);
            else right.add(num);
            if (left.size() > right.size()){
                right.add(center);
                center = left.poll();
            } else if(left.size()+1 < right.size()){
                left.add(center);
                center = right.poll();
            }
            sb.append(center + "\n");
        }
        System.out.println(sb);
    }
}
