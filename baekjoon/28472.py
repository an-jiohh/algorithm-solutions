# 모든 자식 노드 중 노드의 값이 큰 값을 선택
# 다른 사람은 모든 자식 노드 중 노드 중 가장 작은 값을 선택하여 최선의 전략을 찾아보는 방법
# 리프노드의 값은 모두 계산
# 선 플에이어는 Max player로 로트 노드 부터 시작
# 트리에서 리프 노드의 값들은 모두 계산
# 선플레이어는 루트 노드 부터 시작
# 내려갈때마다 번갈아가며 바뀐다.
# MAX Player인 노드의 값은 자식 노드 중 최댓값으로 계산
# MIN Player인 노드의 값은 자식 노드의 값들 중 최솟값으로 계산
# 리프 노드만 있는 상황에서 Minimax트리를 완성
import sys

input = sys.stdin.readline

N, R = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

L = int(input())
node = [-1] * (N+1)
for i in range(1,L+1):
    k, t = map(int, input().split())
    node[k] = t

def dfs(now, parent, position): #Max부터 시작
    global node
    if node[now] != -1 :
        return node[now]
    temp = []
    for next in graph[now] :
        if next != parent :
            temp.append(dfs(next, now, not position))
    if position :
        node[now] = max(temp)
    else :
        node[now] = min(temp)
    return node[now]

dfs(R, R, True)

Q = int(input())
for i in range(Q):
    target = int(input())
    print(node[target])