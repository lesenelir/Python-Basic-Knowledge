row = 1
while row <= 5:
    # 每一行打印的星星和行数一致
    # 增加一个小循环 专门处理当前行中每一列的变量
    col = 1

    while col <= row:
        print("*", end="")
        col = col + 1

    print("") # 这行代码的目的就是在一行星星输出完成之后，添加换行
    row = row + 1
