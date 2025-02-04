def d(i):
    num = i
    split_num = list(map(int, list(str(i))))
    num += sum(split_num)
    return num

max = 10000 + 1
answer = [False] * max

for i in range(1, max+1):
    if d(i) < max :
        answer[d(i)] = True

for i in range(1, max):
    if not answer[i] :
        print(i)
