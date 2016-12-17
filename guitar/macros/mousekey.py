# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar.relpoints import mousekey
from guitar import utils


def left_key():
    utils.moveTo(mousekey.left_key)
    pyautogui.click()


def right_key():
    utils.moveTo(mousekey.right_key)
    pyautogui.click()


def middle_key():
    utils.moveTo(mousekey.middle_key)
    pyautogui.click()


def four_key():
    utils.moveTo(mousekey.four_key)
    pyautogui.click()


def five_key():
    utils.moveTo(mousekey.five_key)
    pyautogui.click()


def scroll_up():
    utils.moveTo(mousekey.scroll_up)
    pyautogui.click()


def scroll_down():
    utils.moveTo(mousekey.scroll_down)
    pyautogui.click()
