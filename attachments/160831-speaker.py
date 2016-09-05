#----speaker.py by me@qzane.com------#
#----2016-08-31----------------------#

import sys
import os

import requests
from lxml import etree

REAL_PATH = os.path.split(os.path.realpath(sys.argv[0]))[0]

CACHE_PATH = os.path.join(REAL_PATH, 'voice')

PLAYER = 'mplayer -volume 100 -softvol -softvol-max 200'

HOST = 'http://dict.cn'
URL = 'http://audio.dict.cn/{}'

CLASS_MALE = 'sound'
CLASS_FEMALE = 'sound fsound'

XPATH = '//i[@class=\'{}\']/@naudio'

USAGE = '''USAGE: python3 {PROGRAM_NAME} [options] word
    (to enable cache, mkdir {CACHE_PATH})
    -h --help, show this message
    -F, Female voice (default)
    -M, Male voice
    -US, US voice (default)
    -UK, UK voice
'''.format(PROGRAM_NAME=sys.argv[0], CACHE_PATH=CACHE_PATH)

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
    return os.path.isfile('{}/{}.mp3'.format(CACHE_PATH, word)) 

def main():
    word = sys.argv[1]
    word_path = os.path.join(CACHE_PATH, '{}.mp3'.format(word))
    if checkVoice(word):
        os.system('{PLAYER} {WORD}'.format(PLAYER=PLAYER, WORD=word_path))
        return 0
    data = getData(word)
    if data == b'':
        print('no voice found')
    else:
        class_name = 'F' if not '-M' in sys.argv else 'M'
        path = 'US' if not '-UK' in sys.argv else 'UK'
        with open('{}.mp3'.format(word),'wb') as f:    
            f.write(getData(word, class_name, path))
        os.system('{PLAYER} {WORD}.mp3'.format(PLAYER=PLAYER, WORD=word))
        os.system('mv {}.mp3 {}'.format(word, word_path))        

if __name__ == '__main__':
    if (len(sys.argv)<2 or
       '-h' in sys.argv or
       '--help' in sys.argv):
        print(USAGE)
    else:
        main()


