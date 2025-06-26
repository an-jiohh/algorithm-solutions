#프로젝트 팀원 수에는 제한이 없다. 
#모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀일 수도 있음
#모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단 한명만)(자기 자신을 선택하는 것도 가능)

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

T = int(input())

for __ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    visited = [False] * (n+1) # 정상적인 깊이우선탐색 흐름
    finished = [False] * (n+1) # 

    answer = 0

    def dfs(node):
        global answer
        visited[node] = True
        nxt = arr[node]
        
        if not visited[nxt] :    
            dfs(nxt)
        elif not finished[nxt] : #싸이클 발생, 현재지점 부터 다시 돌아서 탐색, true면 이미 탐색이 다 끝난 노드를 다시 만났다는 뜻
            temp = nxt
            answer += 1
            while temp != node :
                temp = arr[temp]
                answer += 1
        finished[node] = True # 해당 경로의 탐색이 끝났음
            
    
    for i in range(1, n+1):
        if not visited[i] :
            dfs(i)
    print(n-answer)