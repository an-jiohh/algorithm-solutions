package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Q14907 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";
        Map<String, Integer> node = new HashMap<>();
        Map<String, Integer> increase = new HashMap<>();
        Map<String, List<String>> graph = new HashMap<>();
        while ((input = br.readLine()) != null) {
            String[] index = input.split(" ");
            node.put(index[0], Integer.parseInt(index[1]));
            if(!increase.containsKey(index[0])) increase.put(index[0], 0);
            if(!graph.containsKey(index[0])) graph.put(index[0], new ArrayList<String>());
            if (index.length == 3) {
                for(int i = 0; i < index[2].length(); i++){
                    String temp = String.valueOf(index[2].charAt(i));
                    if(!increase.containsKey(index[0])) increase.put(index[0], 0);
                    increase.put(index[0], increase.get(index[0]) + 1);

                    if(!graph.containsKey(temp)) graph.put(temp, new ArrayList<String>());
                    graph.get(temp).add(index[0]);
                }
            }
        }
        Queue<String> queue = new LinkedList<>();
        Map<String,Integer> dp = new HashMap<>();
        for(String key:node.keySet()){
            if(increase.get(key) == 0){
                queue.add(key);
                dp.put(key, node.get(key));
            }
        }

        
        while(!queue.isEmpty()){
            String now = queue.poll();
            for(String next:graph.get(now)){
                increase.put(next, increase.get(next) - 1);
                dp.put(next, Math.max(dp.getOrDefault(next, 0), dp.getOrDefault(now, 0)+node.get(next)));
                if(increase.get(next)==0){
                    queue.add(next);
                }
            }
        }
        
        System.out.println(dp.keySet().stream().mapToInt(a->dp.get(a)).max().getAsInt());
    }
}
