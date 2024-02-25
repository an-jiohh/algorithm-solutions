s = int(input())

count = 0
for i in range(1,s+2) :
    count += i
    if count >= s :
        print(i-1)
        break