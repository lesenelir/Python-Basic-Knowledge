def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    # 数字累加
    temp = sum_numbers(num - 1)

    # 两个数字的相加
    return num + temp


result = sum_numbers(2)
print(result)