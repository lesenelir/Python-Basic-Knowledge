# 注意：
#   在开发时，应该把所有模块中的所有全局变量和都定义在所有函数上方
#   这样就可以保证所有函数都能正常访问到每一个局部变量了
num = 10
title = "喵宝宝"

def demo():
    print("%d" % num)
    print("%s" % title)
    # print("%s" % name)

# 再定义一个全局变量
# title = "喵宝宝"


demo()


# 再定义一个全局变量
# name = "小明"