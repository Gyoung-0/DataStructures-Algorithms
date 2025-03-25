def solution(L, x):
    answer = []
    isExtinct = False

    for index, value in enumerate(L):
        if value == x:
            answer.append(index)
            isExtinct = True
    if not isExtinct:
        return -1

    return answer    