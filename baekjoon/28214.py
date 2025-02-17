n, k, p = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
check, count = 0, 0

for i in arr :
    count += 1
    if i == 0 : check += 1
    if count == k : 
        if check < p  : 
            answer += 1
        count,check = 0, 0

print(answer)