n = int(input())

numbers = {i:1 for i in input().split()}
m = int(input())
question = [1 if i in numbers else 0 for i in input().split()]

print(*question)