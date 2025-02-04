arr = list(map(int, input().split()))

arr.sort()

a,b,c = arr


m = (a+b) - 1

if c > m :
    c = m

print(a+b+c)