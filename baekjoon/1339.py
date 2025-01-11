'''
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))

count = 9
alpha = {}

arr.sort(key= lambda x:-len(x))

length = len(arr[0])

for i in range(n):
    if len(arr[i]) < length :
        arr[i] = ["_"] * (length - len(arr[i])) + arr[i]

for i in range(length):
    temp = {}
    for j in range(n):
        if len(arr[j]) >= i :
            temp[arr[j][i]] = temp.get(arr[j][i], 0) + 1
    if "_" in temp : del temp["_"]
    while temp :
        check = max(temp, key=temp.get)
        if check in alpha :
            del temp[check]
        else :
            alpha[check] = count
            count -= 1
answer = []
for i in range(n):
    num = ""
    for j in arr[i]:
        if j != "_" : num += str(alpha[j])
    answer.append(int(num))

print(sum(answer))
'''

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))

alpha = {}

for nums in arr :
    count = len(nums) - 1
    for j in range(len(nums)) :
        alpha[nums[count-j]] = alpha.get(nums[count-j], 0) + 10**j

count = 9
answer = []
for i in alpha:
    answer.append(alpha[i])
answer.sort(key=lambda x:-x)

sum = 0
for i in answer:
    sum += count * i
    count -= 1
print(sum)