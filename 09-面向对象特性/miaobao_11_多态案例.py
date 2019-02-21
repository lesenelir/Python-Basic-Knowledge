class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 让狗玩耍
        dog.game()


# 创建狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 创建小明对象
xiaoming = Person("小明")
# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)