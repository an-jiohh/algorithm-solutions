"""
n = int(input())

def d(num):
    sum_num = sum(list(map(int, list(str(num)))))
    if num % sum_num == 0 :
        return True
    return False

count = 0
for i in range(1, n+1) :
    if d(i) :
        count += 1

print(count)
"""

n = int(input())

def d(num):
    snum = str(num)
    temp = 0
    for i in snum :
        temp += int(i)
    if num % temp == 0 :
        return True
    return False

count = 0
for i in range(1, n+1) :
    if d(i) :
        count += 1

print(count)