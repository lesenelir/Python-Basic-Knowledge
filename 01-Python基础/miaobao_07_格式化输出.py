name = "李明"
print("我的名字叫%s，请多多关照" % name)

student_number = 1
print("我的学号是%06d" % student_number) # %06d 表示不到6位用0站位，超过6位该是多少就是多少

price = 8.5
weight = 7.5
money = price * weight
print("苹果的单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" %(price, weight, money))

#格式化输出要输出一个百分号，则在格式化输出的时候需要打上两个百分号，即%%
scale = 0.25
print("数据比列是%.2f%%" % (scale * 100))