import math

t = int(input())
def check():
    m,n = map(int, input().split())
    return math.factorial(n) // (math.factorial(n-m)*math.factorial(m))
    return 

for _ in range(t):
    print(check())