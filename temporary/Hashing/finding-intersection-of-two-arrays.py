
def find_common_elements(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    set1 = set1.intersection(set2)
    return list(set1)


if __name__ == '__main__':
    arr1 = list(map(int, input("Enter arr1 : ").split()))
    arr2 = list(map(int, input("Enter arr2 : ").split()))
    commonElements = find_common_elements(arr1, arr2)
    print(commonElements)
