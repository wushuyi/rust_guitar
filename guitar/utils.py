# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar import point


def moveTo(relpoint):
    p = point.center.abs_point(relpoint)
    pyautogui.moveTo(p.x, p.y)
