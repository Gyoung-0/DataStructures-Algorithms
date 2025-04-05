from array_contains import array_contains
def remove_duplicates(arr):
    if not arr:
        raise ValueError("배열이 비어있습니다.")
    
    answer = [arr[0]]
    for x in arr:
        if not array_contains(answer, x):  # 이 부분을 recursive_contains로 바꿔도 OK
            answer.append(x)
    return answer
