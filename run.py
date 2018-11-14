# coding=utf-8
import itchat, time, random,tuling
from itchat.content import *
import hashlib
print

@itchat.msg_register(TEXT, isFriendChat=True)
def friend_reply(msg):
    datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(u'好友消息 %s %s ： %s' % (datetime, msg.user.remarkName, msg.text))
    # 通过微信上备注的名字，可以定位到某个微信人
    if u"宝贝" in msg.user.remarkName:
        text = u'您好，我是他助理，有急事电话或留言噢~'
        try:
            userid = hashlib.md5(msg.fromUserName).hexdigest()[8:-8]
            text = tuling.robot(content = msg.text, userid = userid)
        except :
            text = u'[强]'
        time.sleep(random.randint(1, 5))
        itchat.send(msg=text, toUserName=msg.fromUserName)
        print(u'send %s to success' % text)


@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(u'群消息 %s %s: %s' % (datetime, msg.actualNickName, msg.text))
    # 接受5分之1的回复
    if random.randint(1, 5) == 5:
        time.sleep(random.randint(1, 5))
        text = u'[强]'
        try:
            text = tuling.robot(content=msg.text, userid=msg.actualNickName)
        except:
            text = u'[强]'
        msg.user.send(u'@%s\u2005 %s' % (
            msg.actualNickName, text))


itchat.auto_login()
itchat.run(True)
