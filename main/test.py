from wxpy import *

bot = Bot()


# classGroup = ensure_one(bot.groups().search("外包2b猴子空调启动通知群⚽"))

@bot.register(Group)
def handle_message(msg):
    if isinstance(msg.sender, Group):
        class_group = msg.sender
        print("是群聊")
        if class_group.name == "外包2b猴子空调启动通知群⚽":
            print("发送人:" + msg.member + " msg:" + msg)
            return '收到消息:{}({})'.format(msg.text, msg.type)

embed()
