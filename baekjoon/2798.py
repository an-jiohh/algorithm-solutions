from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

com_arr = combinations(arr, 3)

answer = 0

for i in com_arr :
    temp = sum(i)
    if temp <= m and answer < temp :
        answer = temp
print(answer)