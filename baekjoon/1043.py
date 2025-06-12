# 파티에서 이야기를하는데, 진실을 말하거나 과장해서 말함
# 하지만 거짓말쟁이로 알려지기싫음, 진실을 아는 사람이 왔을때는 진실을 이야기해야함
# 어떤 파티에서 진실을듣고, 다른데서 과장된이야기를 들으면 거짓말쟁이로 알려짐
# 이런일을 방지하기 위해 모든파티에 참여하되, 과장된 이야기를 할 수 있는 파티의 최댓값을 구하는 문제
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m  = map(int, input().split())


truth = list(map(int, input().split()))

root = [i for i in range(n+1)]
rank = [1] * (n+1)
party_list = [list(map(int, input().split())) for i in range(m)]
party_list.sort(key=lambda x:len(x))

def find(x):
    if root[x] != x :
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if rank[root_x] < rank[root_y]:
        root[root_x] = root_y
    else :
        root[root_y] = root_x
        if rank[root_x] == rank[root_y] :
            rank[root_x] += 1

for i in range(1, len(truth)): #0을 아는 사람들의 집합으로 사용
    union(0, truth[i])
answer = 0
for party in party_list:
    check = False
    for j in range(1, len(party)):
        people = party[j]
        if find(0) == find(people):
            check = True
            break
    if check :
        for j in range(1, len(party)):
            people = party[j]
            union(0, people)
truth_node = find(0)
for party in party_list:
    check = 1
    for j in range(1, len(party)):
        people = party[j]
        if truth_node == find(people) :
            check = 0
    answer += check
print(answer)
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m  = map(int, input().split())


truth = list(map(int, input().split()))

root = [i for i in range(n+1)]
rank = [1] * (n+1)
party_list = [list(map(int, input().split())) for i in range(m)]

def find(x):
    if root[x] != x :
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if rank[root_x] < rank[root_y]:
        root[root_x] = root_y
    else :
        root[root_y] = root_x
        if rank[root_x] == rank[root_y] :
            rank[root_x] += 1

for party in party_list :
    for i in range(1, len(party)-1):
        union(party[i], party[i+1])

truth_root = set()
for i in truth[1:] :
    truth_root.add(find(i))

answer = 0
for party in party_list:
    if find(party[1]) not in truth_root :
        answer += 1
print(answer)