def sum_number(num):
    print(num)
    # 递归函数一定要有递归的出口，如果没有递归的出口，会出现死循环
    # 递归函数的出口当参数满足某个条件时，不再被执行
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)

sum_number(3)