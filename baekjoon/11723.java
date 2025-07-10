package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

class Q11723 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int M = Integer.parseInt(br.readLine());
        Set<Integer> set = new HashSet<>();

        for(int i = 0; i < M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int x = 0;
            if (st.hasMoreTokens()){
                x = Integer.parseInt(st.nextToken());
            }
            if (cmd.equals("add")) {
                set.add(x);
            } else if (cmd.equals("remove")){
                set.remove(x);
            } else if (cmd.equals("check")){
                if (set.contains(x)) sb.append("1\n");
                else sb.append("0\n");
            } else if (cmd.equals("toggle")){
                if (set.contains(x)) set.remove(x);
                else set.add(x);
            } else if (cmd.equals("all")){
                set = new HashSet<>();
                fillSet(set);
            } else if (cmd.equals("empty")){
                set = new HashSet<>();
            }
        }
        System.out.print(sb);
    }
    private static void fillSet(Set<Integer> set){
        for(int i = 1; i <= 20; i++){
            set.add(i);
        }
    }
}

/* 
boolean 배열을 사용
class Q11723 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int M = Integer.parseInt(br.readLine());
        boolean[] set = new boolean[21];

        for(int i = 0; i < M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int x = 0;
            if (st.hasMoreTokens()){
                x = Integer.parseInt(st.nextToken());
            }
            if (cmd.equals("add")) {
                set[x] = true;
            } else if (cmd.equals("remove")){
                set[x] = false;
            } else if (cmd.equals("check")){
                if (set[x]) sb.append("1\n");
                else sb.append("0\n");
            } else if (cmd.equals("toggle")){
                set[x] = !set[x];
            } else if (cmd.equals("all")){
                Arrays.fill(set, true);
            } else if (cmd.equals("empty")){
                Arrays.fill(set, false);
            }
        }
        System.out.println(sb);
    }
}
*/