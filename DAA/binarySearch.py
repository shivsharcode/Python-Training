

def binary_search(arr, elem):
    left = 0
    right = len(arr)-1

    while left < right:
        mid = (left + right)//2
        if arr[mid] < elem:
            # element in right half
            left = mid + 1
        elif arr[mid] > elem :
            # element in left half
            right = mid - 1
        elif arr[mid] == elem:
            print(f"Element founded at index {mid} of the array ")
            return mid

    print("Element not present in the array :( ")
    return -1




if __name__ == '__main__':
    arr = list(map(int, input("Enter array : ").split()))
    # sorting array
    arr.sort()
    elem = int(input("Enter the element to search : "))
    elem_ind =  binary_search(arr, elem)

