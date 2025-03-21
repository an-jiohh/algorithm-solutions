from collections import deque

s, p = map(int, input().split())

dna = list(input())

a,c,g,t = map(int, input().split())

check = {"A":a, "C":c, "G":g, "T":t}
count = {"A":0, "C":0, "G":0, "T":0}

sw = deque()
answer = 0

for i in dna :
    sw.append(i)    
    count[i] +=1
    if len(sw) > p :
        temp = sw.popleft()
        count[temp] -= 1
    if len(sw) == p :
        togle = 0
        for k in count :
            if count[k] < check[k] :
                togle = 1
        if togle == 0 : answer += 1
print(answer)