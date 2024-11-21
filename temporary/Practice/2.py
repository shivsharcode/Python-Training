from collections import Counter
from math import comb


class Solution:
    def countPairs(self, n, arr, k):
        # code here
        mydict = Counter(arr)
        pairs = 0
        for ind, num in enumerate(arr):
            # print(f"Num = {num}")
            i = 1
            while i * k <= num:
                diff = num - i * k
                if diff in mydict:
                    pairs += mydict[diff]
                    # print(num , diff)

                i += 1

        zero_diff = 0
        for i in mydict.values():
            if i > 1:
                zero_diff_comb = comb(i, 2)
                zero_diff += zero_diff_comb

        return pairs + zero_diff
