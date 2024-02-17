'''
# 완전탐색 풀이
n = int(input())

building = list(map(int, input().split()))

for i in range(n) :
    pre_stack = [i]
    post_stack = [i]
    for j in range(i, -1, -1) :
        if building[pre_stack[-1]] < building[j] :
            pre_stack.append(j)
    for j in range(i+1, n) :
        if building[post_stack[-1]] < building[j] :
            post_stack.append(j)
    print(len(pre_stack)+len(post_stack)-2, end=" ")
    temp = []
    if len(pre_stack) > 1 : temp.append(pre_stack[1])
    if len(post_stack) > 1 : temp.append(post_stack[1])
    if temp : print(min(temp)+1, end="")
    print("")
'''

import sys

print = sys.stdout.write

n = int(input())

building = list(map(int, input().split()))


pre_stack = []
length = [0] * n
near = [[] for i in range(n)]

for i in range(n) :
    while pre_stack and building[pre_stack[-1]] <= building[i] :
        pre_stack.pop()
    length[i] += len(pre_stack)
    if pre_stack :
        near[i].append(pre_stack[-1])
    pre_stack.append(i)

post_stack = []
right = []
for i in range(n-1, -1, -1) :
    while post_stack and building[post_stack[-1]] <= building[i] :
        post_stack.pop()
    if post_stack :
        near[i].append(post_stack[-1])
    length[i] += len(post_stack)
    post_stack.append(i)

for i in range(n) :
    print(str(length[i]) + " ")
    if near[i] :
        print(str(min(near[i], key=lambda x:[abs(x-i),x])+1))
    print("\n")

