def linear_search(passed_arr, target):
    for ind, num in enumerate(passed_arr):
        if num == target:
            print("Target Founded at : ", ind)
            return ind

    print("Target Not Founded")
    passed_arr.append(100)
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 2, 9]
    print(arr)
    target = int(input("Enter target : "))
    linear_search(arr, target)
    print(arr)
