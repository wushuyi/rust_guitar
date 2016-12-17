# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar import point, utils
from guitar.relpoints import relmouse as relmouse_points

X_INPUT = None
Y_INPUT = None


def set_x(num):
    global X_INPUT
    if X_INPUT != num:
        utils.moveTo(relmouse_points.x_input)
        pyautogui.doubleClick()
        pyautogui.typewrite('0')
        if num < 0:
            utils.moveTo(relmouse_points.x_minus)
            pyautogui.click()
        else:
            utils.moveTo(relmouse_points.x_add)
            pyautogui.click()
        utils.moveTo(relmouse_points.x_input)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(num))
    X_INPUT = num


def set_y(num):
    global Y_INPUT
    if Y_INPUT != num:
        utils.moveTo(relmouse_points.y_input)
        pyautogui.doubleClick()
        pyautogui.typewrite('0')
        if num < 0:
            utils.moveTo(relmouse_points.y_minus)
            pyautogui.click()
        else:
            utils.moveTo(relmouse_points.y_add)
            pyautogui.click()
        utils.moveTo(relmouse_points.y_input)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(num))
    Y_INPUT = num


def add_macro():
    utils.moveTo(relmouse_points.add_macro)
    pyautogui.click()


def add_relmouse(x, y):
    set_x(x)
    set_y(y)
    add_macro()


if __name__ == '__main__':
    add_relmouse(-1234, 1234)

    pyautogui.easeInQuad
