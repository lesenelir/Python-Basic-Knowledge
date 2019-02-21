# input()函数 得到的是字符串类型
price_str = input("苹果的单价：")
weight_str = input("苹果的重量：")

# 强制类型转换把string类型转换为float类型
price = float(price_str)
weight = float(weight_str)

# 计算付款金额
money = weight * price

#只要买苹果就返五块钱
money = money - 5
print("苹果的单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" %(price, weight, money))
