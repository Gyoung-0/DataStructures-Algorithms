def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i-1

        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        
        L[j+1] = key

    return L
            