n = int(input())
data = list(map(int, input().split()))
result = 0

for fear in data :
    if n > 0 :
        n -= fear
        result += 1
    else :
        break

print(result)