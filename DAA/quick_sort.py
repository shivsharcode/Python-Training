
def quick_sort(arr):
    iterator = [1]  # Using a list to make it mutable and accessible in nested functions
    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                # swap
                arr[j], arr[i] = arr[i], arr[j]

        # final swap
        arr[i+1], arr[high] = arr[high], arr[i+1]
        pivot_index = i+1
        return pivot_index

    def quick_sort_recursive(low, high):
        print(f"Q.S recursion - {iterator[0]}")
        print(arr)
        iterator[0] += 1
        if low < high:
            print("Partioning now ....")
            pivot_index = partition(low, high)
            print("Partition done : pivot index = ", pivot_index)
            print("low to pi - 1")
            quick_sort_recursive(low, pivot_index-1)
            print("pi + 1 to high")
            quick_sort_recursive(pivot_index+1, high)
            print("done here")

    quick_sort_recursive(0, len(arr)-1)
    return arr


if __name__ == '__main__':
    arr = list(map(int, input("Enter array : ").split()))
    print("Original array : ", arr)
    # quick sort
    sorted_array = quick_sort(arr)
    print("Sorted array : ", sorted_array)
