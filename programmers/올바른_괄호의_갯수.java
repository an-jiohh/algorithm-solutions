package programmers;

public class 올바른_괄호의_갯수 {
    int answer = 0;
    public int solution(int n) {
        dfs(0,0,n);
        return answer;
    }
    
    public void dfs(int v, int count, int n) {
        if(count == n * 2) {
            if(v == 0) answer++;
            return;
        }
        if(v < 0) return;
        dfs(v - 1, count + 1, n);
        dfs(v + 1, count + 1, n);
    }
}
