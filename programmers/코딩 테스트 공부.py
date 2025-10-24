# 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하는 문제

def solution(alp, cop, problems):
    max_alp = max([p[0] for p in problems])
    max_cop = max([p[1] for p in problems])
    
    # 초기 능력이 목표 상한보다 클 경우 오류 발생(공부를안해도 모든 문제 풀이 가능시)
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[10**9] * (max_cop + 2) for i in range(max_alp + 2)]
    dp[alp][cop] = 0
    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
                if alp_req <= a and cop_req <= c :
                    temp_a = min(max_alp, a + alp_rwd)
                    temp_c = min(max_cop, c + cop_rwd)
                    dp[temp_a][temp_c] = min(dp[temp_a][temp_c], dp[a][c] + cost)
    return dp[max_alp][max_cop]