# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar.relpoints import delay
from guitar import utils
from guitar.images import keydown_path, keyup_path

KEYDOWN = False
KEYUP = False
NOW_UNIT = None
TIME_INPUT = None

if pyautogui.locateOnScreen(keydown_path):
    KEYDOWN = True

if pyautogui.locateOnScreen(keyup_path):
    KEYUP = True


def key_down(select):
    if KEYDOWN != select:
        utils.moveTo(delay.key_down)
        pyautogui.click()


def key_up(select):
    if KEYUP != select:
        utils.moveTo(delay.key_up)
        pyautogui.click()


def time_input(num):
    global TIME_INPUT
    if TIME_INPUT != num:
        utils.moveTo(delay.time_input)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(num))
    TIME_INPUT = num


def time_add():
    utils.moveTo(delay.time_add)
    pyautogui.click()


def time_minus():
    utils.moveTo(delay.time_minus)
    pyautogui.click()


def unit_millisecond():
    global NOW_UNIT
    if NOW_UNIT != 'millisecond':
        utils.moveTo(delay.unit_select)
        pyautogui.click()
        utils.moveTo(delay.unit_millisecond)
        pyautogui.click()
        NOW_UNIT = 'millisecond'


def unit_sec():
    global NOW_UNIT
    if NOW_UNIT != 'sec':
        utils.moveTo(delay.unit_select)
        pyautogui.click()
        utils.moveTo(delay.unit_sec)
        pyautogui.click()
        NOW_UNIT = 'sec'


def unit_min():
    global NOW_UNIT
    if NOW_UNIT != 'min':
        utils.moveTo(delay.unit_select)
        pyautogui.click()
        utils.moveTo(delay.unit_min)
        pyautogui.click()
        NOW_UNIT = 'min'


def add_macro():
    utils.moveTo(delay.add_macro)
    pyautogui.click()


def add_delay(num, unit='millisecond'):
    time_input(str(num))
    if unit == 'millisecond':
        unit_millisecond()
    elif unit == 'sec':
        unit_sec()
    elif unit == 'min':
        unit_min()
    add_macro()


if __name__ == '__main__':
    add_delay(900)
