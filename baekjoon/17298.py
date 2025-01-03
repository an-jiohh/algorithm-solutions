n = int(input())

arr = list(map(int, input().split()))

arr.reverse()

stack = []
answer = []
for i in arr :
    while stack :
        if stack[-1] <= i :
            stack.pop()
        else :
            break
    if len(stack) == 0 :
        answer.append(-1)
        stack.append(i)
    else :
        answer.append(stack[-1])
        stack.append(i)
answer.reverse()
print(*answer)