n, s = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
sum_num = 0
answer = n + 1 #n으로 최댓값 설정시 start = 0, end = n일때 마지막 조건에서 걸림

while True :
    if sum_num >= s :
        answer = min(answer, end - start)
        sum_num -= arr[start]
        start += 1
    else :
        if end == n :
            break
        sum_num += arr[end]
        end += 1

if answer == n + 1 : answer = 0
print(answer)