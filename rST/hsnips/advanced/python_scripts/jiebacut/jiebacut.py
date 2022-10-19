import jieba
import sys
import os
from pathlib import Path


jsw = Path(__file__).parent / 'jieba_stop_words.txt'

with open(jsw, 'r', encoding='utf8') as fr:
    stop_words = set([x.strip('\n') for x in fr])


def jiebaCut(sentence):

    # ref=https://github.com/fxsjy/jieba/issues/169#issuecomment-49504512

    _result = jieba.lcut_for_search(sentence)
    _result = filter(lambda x: x.lower() not in stop_words, _result)
    result = ','.join(set(_result))
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        s = ''.join(sys.argv[1:])
        print(jiebaCut(s))
    else:
        infor = 'ERROR! NO ARGUMENTS PASSED TO THE SCRIPT!'
        print(infor)
