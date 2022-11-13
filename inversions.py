def sort_count_inversions(A):
    if len(A)<= 1:
        return (A,0)

    # Finding the mid of the array
    mid = len(A) // 2

    (L,x) = sort_count_inversions(A[:mid])

    # Sorting the second half
    (R,y) = sort_count_inversions(A[mid:])

    # now combine
    (sorted_A, z) = merge(L, R)
    return (sorted_A, x+y+z)


def merge(L, R):
    thisInversion = 0
    i = j = k = 0
    merged_A = [0]*(len(L)+len(R))

    # Copy data from arrays L[] and R[] in order
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            merged_A[k] = L[i]
            i += 1
        else:
            thisInversion += (len(L) - i)
            merged_A[k] = R[j]
            j += 1
        k += 1

    # Copying any element that was left
    while i < len(L):
        merged_A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        merged_A[k] = R[j]
        j += 1
        k += 1

    return (merged_A, thisInversion)



if __name__ == "__main__":
    lst = [3,2,1,4,0]
    S, count = sort_count_inversions(lst)
    print(count)  # should be 7
