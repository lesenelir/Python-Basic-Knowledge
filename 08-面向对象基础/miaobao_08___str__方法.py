class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    # 开发时，希望打印自定义内容，可以使用__str__这个内置方法
    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom 是一个全局变量
tom = Cat("汤姆")
print(tom)

