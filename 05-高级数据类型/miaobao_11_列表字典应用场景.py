
# 将多个字典放在一个列表中，进行遍历，列表是个有序的数据集合
card_list = [
    {"name": "张三",
     "qq":"12345",
     "phone": "110"},
    {"name": "李四",
     "qq":"54321",
     "phone": "10086"}
]

for card_info in card_list:
    print(card_info)