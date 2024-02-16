dict = {}

n = int(input())
input_numbers = list(map(int, input().split()))

for i in input_numbers :
    dict[i] = dict.get(i,0) + 1

m = int(input())
answer_numbers = list(map(int, input().split()))
for i in answer_numbers :
    print(dict.get(i,0), end=" ")