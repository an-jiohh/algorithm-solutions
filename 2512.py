n = int(input())

budgets = list(map(int, input().split()))
budget = int(input())

a, b = 0, max(budgets)
while a < b :
    mid = (a+b+1) // 2
    count = 0
    for i in budgets :
        if i < mid :
            count += i
        else :
            count += mid
    if count <= budget : a = mid 
    else : b = mid - 1
print(a)