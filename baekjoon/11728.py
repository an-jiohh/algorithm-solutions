#투포인터를 사용한 풀이
an, bn = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

n = an + bn
a_pointer, b_pointer = 0,0
answer = []

for i in range(n) :
    if a_pointer == an :
        answer.append(b[b_pointer])
        b_pointer += 1
    elif b_pointer == bn :
        answer.append(a[a_pointer])
        a_pointer += 1
    elif a[a_pointer] >= b[b_pointer] :
        answer.append(b[b_pointer])
        b_pointer += 1
    elif a[a_pointer] < b[b_pointer]:
        answer.append(a[a_pointer])
        a_pointer += 1
print(*answer)

#deque를 사용한 풀이
'''
from collections import deque
an, bn = map(int, input().split())

a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

n = an+bn
answer = []

while a and b :
    if a[0] <= b[0] : answer.append(a.popleft())
    else : answer.append(b.popleft())
while a :
    answer.append(a.popleft())
while b :
    answer.append(b.popleft())

print(*answer)
'''

#더해서 정렬하는 풀이
'''
an, bn = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = a+b
answer.sort()
print(*answer)
'''
