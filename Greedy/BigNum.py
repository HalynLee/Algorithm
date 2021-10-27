# n, m, k 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 리스트에서 max값 찾기
maxNum = max(data)
data.remove(maxNum)

# 리스트에서 max값 제외하고 다음으로 큰 수 찾기
newMax = max(data)

result = 0

for i in range(m) :
    if (i%k == 0) and (i != 0):
        result += newMax
    else :
        result += maxNum

print(result)