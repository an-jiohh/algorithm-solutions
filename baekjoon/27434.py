import sys 
sys.setrecursionlimit(10**6)

n = int(input())

def fact(n):
    if n == 0 :
        return 1
    return n * fact(n-1)

print(fact(n))