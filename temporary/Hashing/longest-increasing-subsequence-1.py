# O(n log(n) )
from bisect import bisect_left


def longest_increasing_subsequence(nums):
    n = len(nums)
    tailTable = []

    for val in nums:
        ind = bisect_left(tailTable, val)

        if ind == len(tailTable):
            tailTable.append(val)
        else:
            tailTable[ind] = val

    return len(tailTable)


if __name__ == '__main__':
    nums = list(map(int, input("Enter your array : ").split()))
    res = longest_increasing_subsequence(nums)
    print(res)
