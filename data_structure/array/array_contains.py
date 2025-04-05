def array_contains(arr, value):
    if not arr:
        raise ValueError("배열이 비어있습니다.")
    
    for x in arr:
        if value == x:
            return True
        
    return False

def recursive_contains(arr, value):
    if not arr:
        return False
    if arr[0] == value:
        return True
    
    return recursive_contains(arr[1:], value)