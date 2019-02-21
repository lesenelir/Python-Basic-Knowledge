def sum_2_num(num1, num2):
    """对两个数字的求和"""
    result = num1 + num2

    return result # return 表示函数下方的代码不会再执行


#可以使用变量来接受函数执行的返回结果
sum_result = sum_2_num(10,20)
print("计算的结果:%d" % sum_result)