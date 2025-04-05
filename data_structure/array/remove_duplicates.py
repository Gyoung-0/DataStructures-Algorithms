from array_contains import array_contains
def remove_duplicates(arr):
    if not arr:
        raise ValueError("배열이 비어있습니다.")
    
    answer = [arr[0]]
    for x in arr[1:]:
        if not x in answer:
            answer.append(x)
    return answer

def remove_recursive(arr, idx=0, answer=None):
    if answer is None:
        answer = []

    if not arr:
        return []
    
    if idx == len(arr):
        return answer
    
    if arr[idx] not in answer:
        answer.append(arr[idx])

    return remove_recursive(arr, idx+1, answer)
