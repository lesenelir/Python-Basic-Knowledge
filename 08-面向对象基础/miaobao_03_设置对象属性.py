class Cat:
    """这个一个猫类"""
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用。即：self是当前调用方法的对象自己
        # 在方法内部：
        #   可以通过self. 访问对象的属性，也可以通过self. 调用其他对象方法
        print("%s 爱吃鱼" % self.name)
    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名 利用赋值语句就可以在外部实现设置属性
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

# 再创建一个猫对象
lazy_cat = Cat()

# 可以使用 .属性名 利用赋值语句就可以在外部实现设置属性
lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

# 再创建一个猫对象
lazy_cat2 = lazy_cat # 引用是同一个对象
print(lazy_cat2)