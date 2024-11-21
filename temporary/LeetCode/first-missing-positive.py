class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # DATA CLEAN UP APPROACH
        n = len(nums)

        if 1 not in nums:
            return 1

        # data cleaning converting negatives and values > n into '1'
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # index acts as = hash keys
        # and the -1 sign will act as the presence of val(index) in array

        for i in nums:
            val = abs(i)
            if val == n:
                # suppose an array of 10, will have 0->9 index only but if the array has 10 in it then it would be a
                # problem of assign neg to nums[10] as it would be out of range. At the same time nums[0] is useless
                # thus we'll consider the presence of val = n at the index of 0.
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        # finding the smallest pos value not in the array by finding the first pos occurence
        for i in range(1, n):
            if nums[i] > 0:
                return i

        return n+1  # i.e. when all the number from 1->n are present in the array then the smallest is ought to be n+1


if __name__ == '__main__':
    input_list = list(map(int, input("Enter the array : ").split()))
    solution = Solution()
    result = solution.firstMissingPositive(input_list)
    print("Result = ", result)
