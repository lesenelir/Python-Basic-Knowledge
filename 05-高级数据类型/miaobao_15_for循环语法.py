for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用了break退出了循环
    # 那么else语法内的语句不会被执行
    print("不会被执行")

print("循环结束")

