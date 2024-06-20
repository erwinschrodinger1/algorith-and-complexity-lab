import math


def merge_sort(A: list, p, r):
    # A = array to be sorted
    # p = starting index initially 0
    # r = position till where the array to be sorted initially length-1
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A: list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p : p + n1]
    R = A[q + 1 : q + n2 + 1]
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
