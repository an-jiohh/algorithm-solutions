"""
n = int(input())

arr = [0 for i in range(15)]
count = 0

def promissing(row) :
    for j in range(row) :
        if(arr[row] == arr[j] or row - j ==abs(arr[row]-arr[j])) :
            return False
    return True

def dfs(row) :
    global count
    if row == n :
        count += 1
        return
    for i in range(n) :
        arr[row] = i
        if promissing(row) :
            dfs(row + 1)
        arr[row] = i - 1
dfs(0)
print(count)
"""
n = int(input())

arr = [0] * n #0으로 정해도되는 이유 -> index0은 어차피 dfs에서 처음으로 값이 채워짐
answer = 0

def check(row):
    for i in range(row):
        if arr[i] == arr[row] : #같은 열에 퀸이 존재하는 경우
            return False
        if row - i == abs(arr[row]-arr[i]) :
            return False
    return True

def dfs(row):
    if row == n :
        return 1
    answer = 0
    for i in range(n):
        arr[row] = i 
        if check(row) :
            answer += dfs(row + 1)
    return answer

print(dfs(0))
        