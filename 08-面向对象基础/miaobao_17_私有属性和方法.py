class Women:
    def __init__(self, name):
        self.name = name
        # 定义私有，增加两个下划线 __
        self.__age = 18

    def __secret(self):
        # 在对象方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


CY = Women("小烨")

# 私有属性在外界不能直接被访问
# print(CY.__age)
# 私有方法也不可以在外界直接访问
# CY.__secret()
