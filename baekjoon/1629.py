# a,b,c = map(int, input().split())

# print(pow(a,b,c))

a,b,c = map(int, input().split())

def dfs(a,b):
    if b == 1 :
        return a % c
    
    answer = dfs(a, b // 2)

    if b % 2 == 0 :
        return (answer * answer) % c
    else :
        return (answer * answer) * a % c
    
print(dfs(a,b))