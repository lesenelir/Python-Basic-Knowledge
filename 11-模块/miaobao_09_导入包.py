import miaobao_message

# 包名.文件名.函数
miaobao_message.send_message.send("hello")

txt = miaobao_message.receive_message.receive()
print(txt)