def reverse_array(arr):
    if not arr:
        raise ValueError("값이 비어있습니다")
    reverse = []
    for i in range(len(arr)-1, -1, -1):
        reverse.append(arr[i])
    return reverse

def recursive_reverse(arr):
    if not arr:
        return []
    
    return recursive_reverse(arr[1:]) + [arr[0]] # 리스트로 감싸는 이유는 리스트+리스트가 되어야 리스트끼리 합쳐지기 때문
