# itchat

[![py27][py27] ![py35][py35] [English version][english-version]

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。
增加图灵智能回复，支持个人微信回复，微信群回复，公众号回复

## 安装

可以通过本命令安装itchat：

```python
pip install itchat
```

## 简单入门实例

程序中 **run.py** 是接入图灵机器人的自动回复，可以自己尝试启动程序

有了itchat，如果你想要给文件传输助手发一条信息，只需要这样：

```python
import itchat

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
```

如果你想要回复发给自己的文本消息，只需要这样：

```python
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()
```


一些进阶应用可以在下面的开源机器人的源码和进阶应用中看到，或者你也可以阅览[文档][document]。

### 各类型消息的注册

通过如下代码，微信已经可以就日常的各种信息进行获取与回复。

```python
import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

itchat.auto_login(True)
itchat.run(True)
```

## 常见问题与解答

Q: 如何通过这个包将自己的微信号变为控制器？

A: 有两种方式：发送、接受自己UserName的消息；发送接收文件传输助手（filehelper）的消息

Q: 为什么我发送信息的时候部分信息没有成功发出来？

A: 有些账号是天生无法给自己的账号发送信息的，建议使用`filehelper`代替。


## 类似项目

[youfou/wxpy][youfou-wxpy]: 优秀的api包装和配套插件，微信机器人/优雅的微信个人号API

[liuwons/wxBot][liuwons-wxBot]: 类似的基于Python的微信机器人

[zixia/wechaty][zixia-wechaty]: 基于Javascript(ES6)的微信个人账号机器人NodeJS框架/库

[sjdy521/Mojo-Weixin][Mojo-Weixin]: 使用Perl语言编写的微信客户端框架，可通过插件提供基于HTTP协议的api接口供其他语言调用

[HanSon/vbot][HanSon-vbot]: 基于PHP7的微信个人号机器人，通过实现匿名函数可以方便地实现各种自定义的功能

[yaphone/itchat4j][yaphone-itchat4j]: 用Java扩展个人微信号的能力

[kanjielu/jeeves][kanjielu-jeeves]: 使用springboot开发的微信机器人


[gitter-picture]: https://badges.gitter.im/littlecodersh/ItChat.svg
[gitter]: https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
[py35]: https://img.shields.io/badge/python-3.5-red.svg
[english-version]: https://github.com/littlecodersh/ItChat/blob/master/README_EN.md
[itchatmp]: https://github.com/littlecodersh/itchatmp
[document]: https://itchat.readthedocs.org/zh/latest/
[tutorial2]: http://python.jobbole.com/86532/
[robot-source-code]: https://gist.github.com/littlecodersh/ec8ddab12364323c97d4e36459174f0d
[robot-qr]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/
[robot-demo-file]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87.png?imageView/2/w/300/
[robot-demo-login]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/450/
[littlecodersh]: https://github.com/littlecodersh
[tempdban]: https://github.com/tempdban
[Chyroc]: https://github.com/Chyroc
[youfou-wxpy]: https://github.com/youfou/wxpy
[liuwons-wxBot]: https://github.com/liuwons/wxBot
[zixia-wechaty]: https://github.com/zixia/wechaty
[Mojo-Weixin]: https://github.com/sjdy521/Mojo-Weixin
[HanSon-vbot]: https://github.com/hanson/vbot
[yaphone-itchat4j]: https://github.com/yaphone/itchat4j
[kanjielu-jeeves]: https://github.com/kanjielu/jeeves
[issue#1]: https://github.com/littlecodersh/ItChat/issues/1
