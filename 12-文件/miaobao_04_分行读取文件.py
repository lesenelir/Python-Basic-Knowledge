# 打开文件
file = open("README")

# 读取文件
while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text)

# 关闭文件
file.close()
