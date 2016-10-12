---
layout: post
title: Speaker-For-Stardict
---
为StarDict添加(稍微动听一些的TTS发音).

# 目的
StarDict是Linux下最常用的字典软件，并且支持取词功能，尤其是添加了一些词典和真人语音库以后，非常适合英语学习。我会在另一个帖子中分享我比较推荐的几个字典和语音库。<br/>
但是语音库终归是有限的，对于剩下的单词，虽然可以使用espeak这样的TTS发音软件，但音质实在是...还不如没有。于是我想到了用[Dict.cn](http://dict.cn)上的发音。

# 过程
提取发音地址的方法很简单，看下面提供的代码即可。  <br/>
把这份代码保存为 $HOME/.stardict/speaker.py   <br/>
然后在 `StarDict设置>>Dictionary>>Sound` 中   <br/>
把`Use TTS program` 前面的勾打上  <br/>
在 `Commandline` 中填写 `python $HOME/.stardict/speaker.py %s &`即可

# 注意
* Python3或者Python2都可以使用这份代码，但是要安装Requests和lxml这两个第三方库, 通过pip安装即可
* 默认播放器是mplayer，当然用别的也可以，改掉代码中PLAYER变量即可
* 有其它问题可以发邮件联系我

# 代码
``` python
#----speaker.py by me@qzane.com------#
#----2016-08-31----------------------#

import sys
import os

import requests
from lxml import etree

PLAYER = 'mplayer -volume 100 -softvol -softvol-max 200' #turn up the voice

HOST = 'http://dict.cn'
URL = 'http://audio.dict.cn/{}'

CLASS_MALE = 'sound'
CLASS_FEMALE = 'sound fsound'

XPATH = '//i[@class=\'{}\']/@naudio'

USAGE = '''USAGE: python3 {PROGRAM_NAME} [options] word
    -h --help, show this message
    -F, Female voice (default)
    -M, Male voice
    -US, US voice (default)
    -UK, UK voice
'''.format(PROGRAM_NAME=sys.argv[0])

def getVoice(word, class_name='F', path='US'):
    assert(word.isalpha())
    q = requests.get('%s/%s'%(HOST, word))
    w = etree.HTML(q.text)
    
    e = w.xpath(XPATH.format(CLASS_FEMALE if class_name == 'F' else CLASS_MALE))
    
    return None if len(e)==0 else URL.format(e[1] if path == 'US' else e[0])

def getData(word, class_name='F', path='US'):
    url = getVoice(word, class_name, path)
    if url is None:
        return b''
    else:
        data = requests.get(url).content
        return data

def main():
    data = getData(sys.argv[1])
    if data == b'':
        print('no voice found')
    else:
        class_name = 'F' if not '-M' in sys.argv else 'M'
        path = 'US' if not '-UK' in sys.argv else 'UK'
        with open('tmp.mp3','wb') as f:    
            f.write(getData(sys.argv[1], class_name, path))
        os.system('{PLAYER} tmp.mp3'.format(PLAYER=PLAYER))

if __name__ == '__main__':
    if (len(sys.argv)<2 or
       '-h' in sys.argv or
       '--help' in sys.argv):
        print(USAGE)
    else:
        main()
```
