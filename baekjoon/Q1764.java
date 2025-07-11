package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;


public class Q1764 {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(rd.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Boolean> hash = new HashMap<>();
        
        for(int i = 0; i < n; i++){
            String input = rd.readLine();
            hash.put(input, false);
        }
        for(int i = 0; i < m; i++){
            String input = rd.readLine();
            if(hash.containsKey(input)) hash.put(input, true);
        }
        Set<String> set = hash.keySet();
        List<String> answer = new ArrayList<>(set.size());
        for(String key:set){
            if(hash.get(key)) answer.add(key);
        }
        StringBuffer sb = new StringBuffer();
        answer.sort((a,b)->a.compareTo(b));
        System.out.println(answer.size());
        for(String ans:answer){
            sb.append(ans + "\n");
        }
        System.out.println(sb);
    }
}
