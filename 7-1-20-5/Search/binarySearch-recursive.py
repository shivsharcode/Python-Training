def binary_search_recursive(arr, low, high, target):
    if low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
            return binary_search_recursive(arr, low, high, target)
        elif arr[mid] > target:
            high = mid - 1
            return binary_search_recursive(arr, low, high, target)

    return -1


if __name__ == '__main__':
    arr = [1, 3, 2, 2, 9, 18]
    sorted_arr = sorted(arr)
    print(arr)
    target = int(input("Enter target : "))

    res = binary_search_recursive(sorted_arr, 0, len(arr) - 1, target)
    if res == -1:
        print("Target Not founded")
    else:
        print(f"Target Founded at : {res}")
