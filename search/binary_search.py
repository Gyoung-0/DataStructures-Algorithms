def binary_search(L, target):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left+right) // 2

        if L[mid]==target:
            return mid
        #mid 오른쪽에 값이 있다는거
        elif L[mid] < target:
            left = mid + 1 #오른쪽 탐색
        else:
            right = mid - 1 #왼쪽 탐색
    return -1 #값이 없을때

