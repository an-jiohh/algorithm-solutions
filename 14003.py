from bisect import *

n = int(input())

arr = list(map(int, input().split()))
history = [1 for i in range(n)]
cont = [arr[0]]
cont_arr = [[arr[0]]]

for i in range(1, n):
    temp = bisect_left(cont, arr[i])
    if temp == len(cont) : 
        cont.append(arr[i])
    elif cont[temp] > arr[i] : 
        cont[temp] = arr[i]
    history[i] = temp + 1

count = len(cont)
answer = []
for i in range(n-1, -1, -1) :
    if history[i] == count :
        answer.append(arr[i])
        count -= 1
print(len(cont))
print(*answer[::-1])