n = int(input())

arr = list(map(int, input().split()))

history = []

for i in range(n) :
    temp = [0,list()]
    for j in range(i):
        if arr[i] > arr[j] and history[j][0] > temp[0] :
            temp = history[j]
    node = temp[1][:]
    node.append(arr[i])
    history.append((temp[0]+1, node))

answer = max(history)
print(answer[0])
for i in answer[1] : print(i, end=" ")

'''
## node = temp[1][:]를 개선한 코드
n = int(input())

arr = list(map(int, input().split()))

history = []

for i in range(n) :
    temp = (0,[])
    for j in range(i):
        if arr[i] > arr[j] and history[j][0] > temp[0] :
            temp = history[j]
    history.append((temp[0]+1, temp[1] + [arr[i]]))

answer = max(history)
print(answer[0])
print(*answer[1])
'''