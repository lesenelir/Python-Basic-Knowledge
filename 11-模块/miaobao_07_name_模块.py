# 全局变量 函数 类 ，注意：直接执行的代码不是像外界提供工具
# 文件没有缩进的代码，在导入时都会被执行一边
def say_hello():
    print("你好你好，我是say hello")


# 如果直接执行模块，__main__
# __name__用于需要测试模块
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行
    print("小明开发的模块")
    say_hello()