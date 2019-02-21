# 定义好函数表示只封装了这个函数，如果不主动调用，函数是不执行的
name = "小明"


def say_hello(): # 定义函数的时候前后两侧需要增加两个空行
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


# 调用函数
print(name)
say_hello()
print(name)
