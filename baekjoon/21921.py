# 슬라이딩 윈도우를 활용한 풀이
'''
n, x = map(int, input().split())

arr = list(map(int, input().split()))

answer = sum(arr[:x])
node = answer
count = 1
for i in range(x,n) :
    node = node - arr[i-x] + arr[i]
    if node == answer : count += 1
    if node > answer :
        answer = node
        count = 1

if answer == 0 : print("SAD")
else : 
    print(answer)
    print(count)
'''


# 누적합을 이용한 풀이
'''
n, x = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = []

count = 0
for i in arr :
    count += i
    sum_arr.append(count)

answer = sum_arr[x-1]
answer_count = 1
for i in range(x, n):
    node = sum_arr[i] - sum_arr[i-x]
    if node == answer : answer_count += 1
    if node > answer :
        answer = node
        answer_count = 1

if answer == 0 : print("SAD")
else : 
    print(answer)
    print(answer_count)
'''
