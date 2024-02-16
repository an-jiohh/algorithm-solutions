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