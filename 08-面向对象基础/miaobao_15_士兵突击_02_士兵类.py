class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
        # 发射子弹 子弹数量-1
        self.bullet_count -= 1
        # 提示发射信息
        print("[%s] 突突突...[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪 - 新兵没有枪
        self.gun = None

# 创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()

# 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)