import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    temp = int(input())
    while stack :
        if stack[-1] > temp :
            break
        stack.pop()
    stack.append(temp)
print(len(stack))