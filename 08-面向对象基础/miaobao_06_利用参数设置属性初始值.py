class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # 1. 把希望设置的属性值，定义成 __init__ 方法的参数
        # 2. 在方法内部使用 self.属性 = 形参 接收外部传递的参数
        # 3. 在创建对象时，使用 类名(属性1, 属性2...) 调用
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("汤姆")
tom.eat()


lazy_cat = Cat("大懒猫")
lazy_cat.eat()