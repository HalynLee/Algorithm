'''
히든 테스트 케이스 통과 못한 코드

s = '1101'
result = 0

while True :
    newNum = ''
    for i in range(1, len(s)):
        target = s[i-1]
        if s[i] != target:
            newNum += target

    if s[-1] != target:
        newNum += s[-1]

    cnt0 = newNum.count('0')
    cnt1 = newNum.count('1')

    if cnt0 > cnt1:
        newNum = newNum.replace('1', '0', 1)
    else:
        newNum = newNum.replace('0', '1', 1)

    s = newNum
    if len(s) < 1:
        break
    result += 1

print(result)

'''

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))