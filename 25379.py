"""
### 1차 풀이
from collections import deque

n = int(input())

arr = list(map(int, input().split()))

answer1, answer2, answer3, answer4 = 0,0,0,0
count = 0
for i in arr :
    if i % 2 == 0 :
        count += 1
    else :
        answer1 += count
count = 0
for i in arr[::-1] :
    if i % 2 != 0 :
        count += 1
    else :
        answer2 += count

count = 0
for i in arr :
    if i % 2 == 1 :
        count += 1
    else :
        answer3 += count
count = 0
for i in arr[::-1] :
    if i % 2 != 1 :
        count += 1
    else :
        answer4 += count

print(min(answer1, answer2, answer3, answer4))
"""

"""
### 2차 풀이
from collections import deque

n = int(input())

arr = list(map(int, input().split()))

answer1, answer2 = 0,0
count = 0
for i in arr :
    if i % 2 == 0 :
        count += 1
    else :
        answer1 += count

count = 0
for i in arr :
    if i % 2 == 1 :
        count += 1
    else :
        answer2 += count

print(min(answer1, answer2))
"""

### 3차 풀이
from collections import deque

n = int(input())

arr = list(map(int, input().split()))

answer1, answer2 = 0,0
count1, count2 = 0, 0
for i in arr :
    if i % 2 == 0 :
        count1 += 1
        answer2 += count2
    else :
        answer1 += count1
        count2 += 1        

print(min(answer1, answer2))