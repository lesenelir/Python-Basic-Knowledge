class Animal:

    def eat(self):
        print("吃--")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        print("啸天犬汪汪叫")
        # 使用super(). 调用原本在父类中封装的方法
        super().bark()
        print("*&*&*&")


xtq = XiaoTianQuan()
# 子类重写了父类的方法，在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()