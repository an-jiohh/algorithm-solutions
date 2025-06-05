n = int(input())

a = list(map(int, input().split()))

# add, sub, mul, div = map(int, input().split())
cal = list(map(int, input().split()))

max_answer, min_answer = -10**10, 10**10
def dfs(node, count): #node = 1부터 시작
    global max_answer, min_answer
    if node == n - 1 :
        max_answer = max(max_answer, count)
        min_answer = min(min_answer, count)
        return
    for i in range(4):
        if cal[i] > 0 :
            temp = 0
            if i == 0 : temp = count + a[node+1]
            elif i == 1 : temp = count - a[node+1]
            elif i == 2 : temp = count * a[node+1]
            elif i == 3 : 
                if count < 0 : 
                    temp = ((-1 * count) // a[node+1]) * -1
                else : 
                    temp = count // a[node+1]
            cal[i] -= 1
            dfs(node+1, temp)
            cal[i] += 1

dfs(0, a[0])
print(max_answer)
print(min_answer)