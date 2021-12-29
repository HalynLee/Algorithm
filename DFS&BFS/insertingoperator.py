from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
onum = list(map(int, input().split()))

operators = []
max_result = -1e9
min_result = 1e9

for i in range(4):
    for j in range(onum[i]):
        operators.append(i)

cals = list(permutations(operators, len(operators)))

for cal in cals:
    result = 0
    for i in range(len(nums)):
        if i == 0:
            result += nums[i]
            continue
        if cal[i - 1] == 0:
            result += nums[i]
        elif cal[i - 1] == 1:
            result -= nums[i]
        elif cal[i - 1] == 2:
            result *= nums[i]
        else:
            if result < 0:
                result = abs(result) // nums[i]
                result = -(result)
            else:
                result = result // nums[i]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)