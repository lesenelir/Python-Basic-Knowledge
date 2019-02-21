has_ticket = True
knife_length = 30
if has_ticket:
    print("车票检查通过,准备安检")
    if knife_length > 20:
        print("携带的刀太长了，有%d公分长" % knife_length)
        print("不允许上车")
    else:
        print("安检通过，允许上车")
else:
    print("请先买票")