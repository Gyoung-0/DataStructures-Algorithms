def find_min(arr):
    if not arr:
        return None
    
    min_val = arr[0]

    for x in arr:
        if x < min_val:
            min_val = x

    return min_val
