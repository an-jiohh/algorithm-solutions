n = int(input())
count = 0
for i in range(1,n+1):
    for j in list(str(i)):
        if "3" in str(j) or "6" in str(j) or "9" in str(j):
            count += 1
print(count)