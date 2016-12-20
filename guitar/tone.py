# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import sys
import os
from guitar.macros import duration, mousekey, relmouse, delay
import pyautogui

'''
 do re mi fa so la si do
'''

full_y = -1600


def get_y(tone):
    step = full_y / 6
    return int(round(step * tone))


def play():
    delay.key_down(True)
    delay.key_up(True)
    delay.time_input(64)
    mousekey.right_key()


def do():
    duration.durationMove(0, 1600, duration=0.4)
    delay.add_delay(400)
    play()


def re():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(1), duration=0.4)
    play()


def mi():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(2), duration=0.4)
    play()


def fa():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(3), duration=0.4)
    play()


def so():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(4), duration=0.4)
    play()


def la():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(5), duration=0.4)
    play()


def si():
    duration.durationMove(0, 1600, duration=0.4)
    duration.durationMove(0, get_y(6), duration=0.4)
    play()


if __name__ == '__main__':
    do()
    re()
    mi()
    fa()
    so()
    la()
    si()