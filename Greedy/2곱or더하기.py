data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if result + num > result * num :
        result += num
    else :
        result *= num

print(result)
