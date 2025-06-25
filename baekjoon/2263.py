# 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 
# 인오더와 포스트오더 -> 프리오더

# 복습
# Inorder: D B E A F C
# Postorder: D E B F C A
# postorder은 루트를 마지막에 순회하기 때문에 마지막 부터 전체 또는 서브 트리의 루트가 존재
# Inorder은 왼쪽오른쪽에 노드가 무엇인지 알 수 있음
# 두개의 특징을 이용해서 트리 복원가능
import sys
sys.setrecursionlimit(10**9)

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

find_in_order = {}

for i in range(n):
    find_in_order[in_order[i]] = i

def find(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = post_order[post_end]
    root_idx = find_in_order[root]

    print(root, end=" ")

    size = root_idx - in_start

    find(in_start, root_idx - 1, post_start, post_start + size - 1)
    find(root_idx + 1, in_end, post_start + size, post_end - 1)

find(0, n-1, 0, n-1)