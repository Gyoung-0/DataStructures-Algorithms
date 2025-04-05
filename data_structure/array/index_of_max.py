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

print(index_of_max([1, 3, 2, 5, 4]))  # 결과: 3