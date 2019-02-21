def demo1():
    # 局部变量：
    # 出生： 执行调用函数，才被创建
    # 死亡： 函数执行完成之后，局部变量被系统回收
    num = 10  # 局部变量
    print("在demo1函数内部的变量是%d" % num)


def demo2():

    # print("%d" % num ) 函数内部不能调用别的函数变量
    pass


demo1()