# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
from guitar import tone

def noop():
	pass

MY_SONG = '11556654433221' \
          '55443325544332' \
          '11556654433221'

tonelist = [
	noop,
    tone.do,
    tone.re,
    tone.fa,
    tone.so,
    tone.la,
    tone.si
]


def play_song(song):
    song = list(song)
    for i in song:
	    play = tonelist[int(i)]
	    play()
		


if __name__ == '__main__':
    play_song(MY_SONG)
