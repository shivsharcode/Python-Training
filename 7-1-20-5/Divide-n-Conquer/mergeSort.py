def merge(L, R):
    sorted_array = []
    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            sorted_array.append(L[i])
            i += 1

        else:
            sorted_array.append(R[j])
            j += 1

    # append remaining elements of left subarray (if any)
    while i < len(L):
        sorted_array.append(L[i])
        i += 1

    while j < len(R):
        sorted_array.append(R[j])
        j += 1

    return sorted_array



def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # left subarray
    left_part = merge_sort(arr[: mid])
    right_part = merge_sort(arr[mid:])

    return merge(left_part, right_part)


if __name__ == '__main__':
    arr = [2, 3, 8, 1, 1, 9, 11]
    print("arr : ", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted arr : ", sorted_arr)

