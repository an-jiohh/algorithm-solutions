n = int(input())
m = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b :
        m = min(m, b)
if m == 1001 : m = -1
print(m)