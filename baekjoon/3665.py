#  n개의 팀 -> 작년 순위 존재
# 이번해 상대적인 순위가 바뀐 팀의 목록만 발표
# 상대적인 순위가 바뀐 모든 팀의 목록
# 확실한 올해 순위를 만들 수 없는 경우 = IMPOSSIBLE or 일관성이 없는 잘못된 정보 = ?
# ex) 5 -> 4 -> 3 -> 2 -> 1 
# 2 -> 4, 3 -> 4
# 5 -> 3 -> 2 -> 4 -> 1
# 일관성이 없는 잘못된 정보 = 체크했을때 순위가 안바꼇을 경우

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        rank = list(map(int, input().split()))
        graph = [[False] * (N + 1) for _ in range(N + 1)]
        indegree = [0] * (N + 1)

        # 초기 순위 → 간선 생성
        for i in range(N):
            for j in range(i+1, N):
                a, b = rank[i], rank[j]
                graph[a][b] = True
                indegree[b] += 1

        # 순위 변경 적용
        M = int(input())
        for _ in range(M):
            a, b = map(int, input().split())
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[b] -= 1
                indegree[a] += 1
            else:
                graph[b][a] = False
                graph[a][b] = True
                indegree[a] -= 1
                indegree[b] += 1

        # 위상 정렬 시작
        q = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                q.append(i)

        result = []
        certain = True
        cycle = False

        for _ in range(N):
            if not q:
                cycle = True
                break
            if len(q) > 1:
                certain = False

            now = q.popleft()
            result.append(now)
            for i in range(1, N + 1):
                if graph[now][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)

        if cycle:
            print("IMPOSSIBLE")
        elif not certain:
            print("?")
        else:
            print(" ".join(map(str, result)))

solution()