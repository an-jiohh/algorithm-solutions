from collections import deque

s = input()
t = deque(list(input()))
answer = 0
while t :
    if "".join(t) == s :
        answer = 1
        break
    if t[-1] == "A" :
        t.pop()
    elif t[-1] == "B" :
        t.pop()
        t.reverse()
    else :
        break
print(answer)