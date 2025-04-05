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
    
    return recursive_reverse(arr[1:]) + [arr[0]]

print(recursive_reverse(["a", "b", "c"]))  # ['c', 'b', 'a']