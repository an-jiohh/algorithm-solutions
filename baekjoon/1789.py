s = int(input())

count = 0
cnt = 1
for i in range(1,s+2) :
    count += i
    cnt = i
    if count > s :
        break
    
print(cnt-1)