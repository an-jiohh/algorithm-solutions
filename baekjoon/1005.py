# 건물짓는 순서가 정해져 있지 않음, 게임마다 순서가 다름
# 각 건물을 완성시킬때까지 모든 건물 딜레이가 존재
# 규칙 순서가 같은면 동시에 진행가능
# 최소시간을 구하는 문제
# T 테스트 케이스
# N, K 건물, 건설순서 규칙 n <= 1000, k <= 100,000
# D1,D2.... 건물당 걸설에 거리는 시간 D <= 100,000
# X Y 건설 순서 X -> Y순서 
# w 승리해야하는 건물 번호

# 주요관건
# 위상정렬 알고리즘을 사용해야하는가
# dp를 왜 꼭 사용해야하는가

from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split())) #건물을 짓는데 걸리는 시간배열
    edge = [[] for i in range(n+1)] #간선 저장 배열, 노드 -> 다음노드
    counter = [0 for i in range(n+1)] #진입차수 저장
    for i in range(k):
        a,b = map(int, input().split())
        edge[a].append(b)
        counter[b] += 1
    w = int(input())

    dp = [0] * (n + 1) #해당 노드 도착까지의 시간 수(인덱스 = 노드, 원소 = 시간)
    queue = deque()
    for i in range(1, n+1):
        if counter[i] == 0 :
            queue.append(i)
            dp[i] = d[i]
        
    while queue:
        temp = queue.popleft()
        for i in edge[temp]: # i == 다음 노드
            counter[i] -= 1
            dp[i] = max(dp[temp] + d[i],  dp[i]) # 지금 시간 + 건설하는데 걸리는 시간 <> 지금까지 최대 시간
            if counter[i] == 0 :
                queue.append(i)
    print(dp[w])