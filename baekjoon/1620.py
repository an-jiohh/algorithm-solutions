import sys

input = sys.stdin.readline

dict = {}
count = 0
while True :
    temp = input()
    if not temp :
        break
    dict[temp] = dict.get(temp, 0) + 1
    count += 1

for name, cnt in dict :
    print(f'{name}, {(cnt/count*100):%.4f}')