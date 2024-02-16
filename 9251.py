string_a = list(input())
string_b = list(input())
length_a = len(string_a) + 1
length_b = len(string_b) + 1

arr = [[0] * length_b for i in range(length_a)]

for i in range(length_a) :
    for j in range(length_b) :
        if i == 0 or j == 0 : continue
        elif string_a[i-1] == string_b[j-1] :
            arr[i][j] = arr[i - 1][j - 1] + 1
        else :
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(max(arr[-1]))