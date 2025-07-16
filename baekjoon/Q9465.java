package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q9465 {
    private static int max(int x, int y){
        if (x > y) return x;
        else return y;
    }
    private static int max(int[] a){
        return Arrays.stream(a).max().getAsInt(); 
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++){
            int n = Integer.parseInt(br.readLine());
            StringTokenizer aSt = new StringTokenizer(br.readLine());
            StringTokenizer bSt = new StringTokenizer(br.readLine());
            int[] check = new int[3];
            check[1] = Integer.parseInt(aSt.nextToken());
            check[2] = Integer.parseInt(bSt.nextToken());
            for(int i = 1; i < n; i++){
               int a = Integer.parseInt(aSt.nextToken());
               int b = Integer.parseInt(bSt.nextToken());
               int check0 = max(check);
               int check1 = max(check[0],check[2]) + a;
               int check2 = max(check[0],check[1]) + b; 
               check[0] = check0; check[1] = check1; check[2] = check2;
            }
            System.out.println(max(check));
        }
    }
}
