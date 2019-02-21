class Women:
    def __init__(self, name):
        self.name = name
        # 定义私有，增加两个下划线 __
        self.__age = 18

    def __secret(self):
        # 在对象方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


CY = Women("小烨")


# Python只有伪私有属性，可以添加_类名__私有属性/方法 来获得
# 但是Python中，不建议这么做
print(CY._Women__age)

CY._Women__secret()
