def partition(arr, low, high):
    pivot = arr[high]  # set the last element as the pivot
    i = low - 1     # pointer for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            # if elements are smaller than pivot
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    # swap the pivot with the element just after the smaller elements so that partitions are made
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1  # return the pivot index


def quickSort(arr, low, high):
    if low < high:
        pivot_ind = partition(arr, low, high)  # it partitions the elements smaller than the pivot to left and larger than pivot to the right subarray.
        # sort left subarray
        quickSort(arr, low, pivot_ind-1)
        # sort right subarray
        quickSort(arr, pivot_ind+1, high)


if __name__ == '__main__':
    arr = [2, 3, 9, 33, 1, 3, 8]
    print(arr)
    quickSort(arr, 0, len(arr)-1)
    print(f"Sorted arr \n{arr}")
