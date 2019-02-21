class Cat:
    """这个一个猫类"""
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)  # %x 十六进制
print("%d" % addr)  # %d 十进制
