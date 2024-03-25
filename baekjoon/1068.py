n = int(input())

parents_node = list(map(int, input().split()))
delete_node = int(input())
# dfs로 탐색을 시도하고 만약 삭제노드가 나오면 탐색을 안하면됨
answer = 0
def dfs(node):
    global answer
    togle = 1
    for i in range(n) :
        if parents_node[i] == node :
            if i != delete_node :
                dfs(i)
                togle = 0
    answer += togle

for i in range(n) :
    if parents_node[i] == -1 and i != delete_node:
        dfs(i)
        break
print(answer)