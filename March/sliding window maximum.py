from collections import deque
def maxSlidingWindow(li, k):
    dq = deque()
    for i in range(k):
        dq.append(li[i])

    ansList = [max(dq)]
    print(ansList)

    for i in range(k, len(li)):
        dq.append(li[i])  # added new right element
        dq.popleft()  # removed the first element of the window

        # ansList.append(max(dq))  # O(k) --

        

    print(ansList)


if __name__ == '__main__':

    li = list(map(int, input("Enter the list : ").split()))
    k = int(input("Enter k : "))
    maxSlidingWindow(li, k)
