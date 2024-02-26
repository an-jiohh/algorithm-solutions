n = int(input())

answer = n // 5
n = n % 5

while answer >= 0 :
    if n % 2 == 0 :
        answer += (n//2)
        break
    answer -= 1
    n += 5
    if answer < 0 :
        answer = -1
print(answer)