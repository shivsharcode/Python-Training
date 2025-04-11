# class Solution:
#     from collections import deque
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         dq = deque()
#         # initial window
#         for i in range(k):
#             dq.append(nums[i])
#
#         ansList = [max(dq)]  # final list of max elements
#
#         # sliding the window
#         for i in range(k, len(nums)):
#             dq.append(nums[i])  # adding new element
#             dq.popleft()  # removing the left element
#
#             ansList.append(max(dq))
#
#         return ansList