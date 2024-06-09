
for i in range(5):
    for j in range(5):
        print('x', end="")
        if not (i == 0 or i == 2):
            if j >= 1:
                break

    print("")
