import sys
input = sys.stdin.readline

N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

answer, count = 0, 0
if box[0] > crain[0] :
    answer = -1
else :
    while count < M :
        for i in crain :
            if box and i < box[-1] :
                continue
            for j in range(answer, M) :
                if 0 < box[j] <= i :
                    box[j] = 0
                    count += 1
                    break
        answer += 1

print(answer)