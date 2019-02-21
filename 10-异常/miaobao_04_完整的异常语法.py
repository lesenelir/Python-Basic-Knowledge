try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))
    # 使用8除以用书输入的整数并且输出
    result = 8 / num
    print(result)
# python解释器抛出异常时，最后一行错误信息的第一个单词，就是错误类型

except ValueError:
    print("请输入正确的整数")
except Exception as result_except:
    print("未知错误 %s" % result_except)
else:
    print("没有异常才会执行")
finally:
    print("无论是否有异常都会执行")

print("-" * 40)
