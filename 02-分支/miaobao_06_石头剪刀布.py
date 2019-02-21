import random
player = int(input("请输入要出的拳 石头(1) / 剪刀(2) / 布 (3) ："))
computer = random.randint(1, 3)  # 函数参数是随机数选择范围,在randint 1到3选择随机数
print("玩家选择的拳头是%d - 电脑选择的拳头是%d" % (player, computer))
if ((player == 1 and computer == 2)          # if( ()
        or (player == 2 and computer == 3)   #         ()
        or (player == 3 and computer == 1)): #        ()  八个空格方便阅读
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")