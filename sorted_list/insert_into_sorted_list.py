def solution(L, x):
    answer = L.copy()
    allMax = True
    for index, value in enumerate(answer):
        if value > x:
            answer.insert(index, x)
            allMax = False
            break
    if allMax:
        answer.insert(len(answer), x)
        return answer
    return answer