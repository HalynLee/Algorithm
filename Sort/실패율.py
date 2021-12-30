def original_solution(N, stages):
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


def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i) ##

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda t:t[1], reverse=True)

    answer =[i[0] for i in answer]
    return answer
