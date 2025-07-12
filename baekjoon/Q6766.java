package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q6766 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int k = Integer.parseInt(br.readLine());
        String inputText = br.readLine();
        for(int i = 0; i < inputText.length(); i++){
            int target = (int) inputText.charAt(i) + 'A';
            int value = ((target - (3 * (i+1) + k)) + 26) % 26;
            sb.append((char) (value+'A'));
        }
        System.out.println(sb);
        
    }
}
