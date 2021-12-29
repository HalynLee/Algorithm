def solution(N, stages):
    answer = []
    challenger = {index + 1: 0 for index in range(0, N + 1)}
    fail = {index + 1: 0 for index in range(0, N)}
    total = 0

    for user in stages:
        challenger[user] += 1

    for i in range(1, N + 1):
        if total == len(stages):
            fail[i] = -1
        else:
            fail[i] = challenger[i] / (len(stages) - total)
        total += challenger[i]

    return sorted(fail, reverse=True, key=lambda x: fail[x])