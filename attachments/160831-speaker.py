#----speaker.py by me@qzane.com------#
#----2016-08-31----------------------#
#todo: cache directory should be specific

import sys
import os

import requests
from lxml import etree

PLAYER = 'mplayer -volume 100 -softvol -softvol-max 200'

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

def checkVoice(word):
    return os.path.isfile('./voice/{}.mp3'.format(word)) 

def main():
    if(checkVoice(sys.argv[1])):
        os.system('{PLAYER} ./voice/{WORD}.mp3'.format(PLAYER=PLAYER, WORD=sys.argv[1]))
        return 0
    data = getData(sys.argv[1])
    if data == b'':
        print('no voice found')
    else:
        class_name = 'F' if not '-M' in sys.argv else 'M'
        path = 'US' if not '-UK' in sys.argv else 'UK'
        with open('tmp.mp3','wb') as f:    
            f.write(getData(sys.argv[1], class_name, path))
        os.system('{PLAYER} tmp.mp3'.format(PLAYER=PLAYER))
        os.system('mv tmp.mp3 ./voice/{}.mp3'.format(sys.argv[1]))        

if __name__ == '__main__':
    if (len(sys.argv)<2 or
       '-h' in sys.argv or
       '--help' in sys.argv):
        print(USAGE)
    else:
        main()


