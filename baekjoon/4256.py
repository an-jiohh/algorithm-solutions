# 전위 순회 및 중위 순회가 주어질때 후위순회를 구하는 문제
# 전위 순회 3,6,5,4,8,7,1,2
# 중위 순회 5,6,8,4,3,1,2,7
# 답 후위 순회 : 5,8,4,6,2,1,7,3

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

for ___ in range(T):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    find_in_order = {}
    for i in range(n):
        find_in_order[in_order[i]] = i
    def split(in_start, in_end, pre_start, pre_end):
        if in_start > in_end or pre_start > pre_end :
            return
        
        root = pre_order[pre_start]

        root_idx = find_in_order[root]
        size = root_idx - in_start #왼쪽 서브트리

        split(in_start, root_idx - 1, pre_start+1, pre_start+size)
        split(root_idx + 1, in_end, pre_start + size + 1, pre_end)
        print(root, end=" ")
    split(0,n-1,0,n-1)
    print()
