from wxpy import *

bot = Bot()
classGroup = bot.groups().search("外包2b猴子空调启动通知群⚽")[0]


@bot.register(classGroup)
def handle_message(msg):
    print("发送人:" + msg.member)
    return '收到消息:{}({})'.format(msg.text, msg.type)


embed()
