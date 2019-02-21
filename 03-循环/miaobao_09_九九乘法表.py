row = 1
while row <= 9:

    col = 1
    while col <= row:
        # print("*", end="")
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col = col + 1
    print("")
    # print("%d" % row)
    row = row + 1