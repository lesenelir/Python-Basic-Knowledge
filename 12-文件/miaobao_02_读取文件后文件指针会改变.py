# 打开文件
file = open("README")

# 读取文件
text = file.read()
print(text)
print(len(text))

print("-" * 40)

text = file.read()  # 此时文件指针已经移动到了文件末尾，读取不到内容
print(text)
print(len(text))

# 关闭文件
file.close()
