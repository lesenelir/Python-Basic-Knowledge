a = 6
b = 100

# 解法1： - 使用其他变量
# c = a
# a = b
# b = c

# 解法2： - 不实用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法3： - Python专有
# a, b = (b, a) # 多个变量接受元组
a, b = b, a     # 省去括号


print(a)
print(b)
print("-------------")

