n, m = map(int, input().split())  # n - rows, m - cols

table = [[0 for _ in range(m)] for _ in range(n)]

for rowidx in range(n):
    row = list(map(int, input().split()))
    for colidx in range(m):
        table[rowidx][colidx] = row[colidx]

k = int(input())  # score k, we've to find the cells with score k

scoreTable = [[0 for _ in range(m)] for _ in range(n)]  # here I've initialised the scoreTable 2d

# for the first row we'll only check the left to right traverse check and giving the [0][0] node the score of zero bcoz it's not recheable
for col in range(1, m):
    if table[0][col] >= table[0][col - 1]:
        scoreTable[0][col] += scoreTable[0][col - 1] + 1

# for the first column excluding [0][0] we've to check only the traverse check of top--> bottom
for row in range(1, n):
    if table[row][0] >= table[row - 1][0]:
        scoreTable[row][0] += scoreTable[row - 1][0] + 1

# now from second row second column we'll check the left-->right and top-->bottom traverse check
for row in range(1, n):
    for col in range(1, m):
        # left->right check
        if table[row][col] >= table[row][col - 1]:
            scoreTable[row][col] += scoreTable[row][col - 1] + 1

        # top-->bottom check
        if table[row][col] >= table[row - 1][col]:
            scoreTable[row][col] += scoreTable[row - 1][col] + 1

# scoreTable created succ
flag = False
for row in range(n):
    for col in range(m):
        if scoreTable[row][col] == k:
            print(row, col)
            flag = True

if not flag:
    print("NO")
