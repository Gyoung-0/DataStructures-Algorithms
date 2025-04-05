def find_max(arr):
    if not arr:
        return None

    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val