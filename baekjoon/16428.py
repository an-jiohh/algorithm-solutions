a, b = map(int, input().split())

div = a // b
mod = a % b

if mod < 0 :
    div += 1
    mod -= b
print(div)
print(mod)