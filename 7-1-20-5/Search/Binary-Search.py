def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            # update high
            high = mid - 1

        elif arr[mid] < target:
            # update low
            low = mid + 1

    return -1


if __name__ == '__main__':
    arr = [1, 3, 2, 2, 9, 18]
    sorted_arr = sorted(arr)
    print(arr)
    target = int(input("Enter target : "))
    res = binary_search(sorted_arr, target)
    if res == -1:
        print("Target Not founded")
    else:
        print(f"Target founded at {res}")