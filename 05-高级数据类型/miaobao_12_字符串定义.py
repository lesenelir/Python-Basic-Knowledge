str1 = "hello world hello"
str2 = '我的外号是"大西瓜"'

print(str2)
print(str1[6])

for char in str2:
    print(char)

# 统计字符串长度
print(len(str1))

# 统计某一个小字符串出现的次数
print(str1.count("llo"))

# 某一个子字符串出现的位置
print(str1.index("llo"))