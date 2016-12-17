# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar.images import ylxs_path


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%s, %s' % (self.x, self.y)


class RelPoint(Point):
    pass


class CenterPoint(Point):
    def rel_point(self, p):
        nx = p.x - self.x
        ny = p.y - self.y
        return RelPoint(nx, ny)

    def abs_point(self, p):
        nx = self.x + p.x
        ny = self.y + p.y
        return Point(nx, ny)


center = CenterPoint(*pyautogui.locateCenterOnScreen(ylxs_path))
