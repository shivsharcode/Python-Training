def binary_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high-low)//2

        if arr[mid] == target:
            return mid          # target founded
        elif arr[mid] < target:
            low = mid + 1       # search in the right half
        else:
            high = mid - 1      # search in the left half

        return low  # location to be inserted


def longest_