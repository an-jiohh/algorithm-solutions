arr = list(input())
answer = [0] * 26
for i in arr :
    answer[ord(i)-ord('a')] += 1
print(*answer)