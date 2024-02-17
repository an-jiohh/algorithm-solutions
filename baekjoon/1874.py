import sys

input = sys.stdin.readline

stack = []
count = 1
answer = []
n = int(input())

for i in range(n) :
    target = int(input())
    while count <= n and count <= target :
        stack.append(count)
        count += 1
        answer.append("+")
    if stack and stack[-1] > target :
        answer = ["NO"]
        break
    if stack and stack[-1] == target :
        answer.append("-")
        stack.pop()
        
for i in answer :
    print(i)