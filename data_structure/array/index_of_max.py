def index_of_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    max_index = 0
    for i in range(len(arr)):
        if max_val < arr[i]:
            max_val = arr[i]
            max_index = i

    return max_index

def recursive_max_index(arr, idx=0, max_idx=0):
    if not arr:
        return None
    
    if idx == len(arr):
        return max_idx
    
    if arr[idx] > arr[max_idx]:
        max_idx = idx

    return recursive_max_index(arr,idx+1, max_idx)
    