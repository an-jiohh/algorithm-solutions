from bisect import bisect_left

n = int(input())

arr = list(map(int, input().split()))

history = []
memory = []

for i in range(n) :
    temp = bisect_left(memory, arr[i])
    if temp == len(memory) : memory.append(arr[i])
    if memory[temp] > arr[i] : memory[temp] = arr[i]
    history.append(temp+1)


print(max(history))