import sys

input = sys.stdin.readline

n = int(input())
vil = []
people_amount = 0
for i in range(n) :
    x, a = map(int, input().split())
    vil.append((x, a))
    people_amount += a

vil.sort(key=lambda x:x[0])
count = 0
for i in vil :
    x, a = i
    count += a
    if count >= people_amount / 2 :
        print(x)
        break