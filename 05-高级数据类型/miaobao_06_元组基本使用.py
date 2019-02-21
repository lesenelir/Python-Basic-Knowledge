info_tuple = ("张三", 18, 1.75,"张三")

# 取值和取索引
print(info_tuple[0])
print(info_tuple.index("张三")) # 取索引：已经知道数据内容，希望知道该数据在元组中的索引


# 统计计数
print(info_tuple.count("张三"))

# 统计元组中包含元素的个数
print(len(info_tuple))