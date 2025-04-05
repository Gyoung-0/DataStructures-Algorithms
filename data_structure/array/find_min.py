def find_min(arr):
    if not arr:
        return None
    
    min_val = arr[0]

    for x in arr:
        if x < min_val:
            min_val = x

    return min_val

print(find_min([3, 1, 7, 2, 0]))  # Output: 0
print(find_min([-5, -2, -8]))     # Output: -8
print(find_min([]))               # Output: None