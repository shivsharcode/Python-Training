def finding_subarray_with_given_sum(arr, target):
    subarrayList = []
    prefix_sum_dict = dict()   # dictionary with key : {prefix_sum}, value : {index}
    prefix_sum = 0

    n = len(arr)

    for ind, num in enumerate(arr):
        prefix_sum += num

        # checking if we've found a subarray from start
        if prefix_sum == target:
            subarrayList.append(arr[: ind + 1])

        # checking if there is in-between prefix_sum till the current
        if (prefix_sum - target) in prefix_sum_dict:
            startIndex = prefix_sum_dict[prefix_sum - target] + 1
            subarrayList.append(arr[startIndex: ind + 1])

        # storing the current prefix_sum with its index if not already stored
        if prefix_sum not in prefix_sum_dict:
            prefix_sum_dict[prefix_sum] = ind

    return subarrayList


if __name__ == '__main__':
    arr = list(map(int, input("Enter your array : ").split()))
    target = int(input("Enter target sum : "))

    subarrayList = finding_subarray_with_given_sum(arr, target)
    print(subarrayList)
