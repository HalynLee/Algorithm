n = input()
alphabet = []
number = []

for i in range(len(n)):
    if ord(n[i]) >= 65 and ord(n[i]) < 90: # 알파벳이면
        alphabet.append(n[i])
    else: # 숫자일 경우
        number.append(int(n[i]))

alphabet.sort()
result = sum(number)

print(''.join(alphabet) + str(result))