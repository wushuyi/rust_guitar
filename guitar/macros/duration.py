# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/12/17 0017.
import pyautogui
from guitar.macros import delay, relmouse
from pytweening import linear

MINIMUM_DURATION = 0.1
MINIMUM_SLEEP = 0.05


class RelPointOnLine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self, n):
        x = self.x * n
        y = self.y * n
        return int(round(x)), int(round(y))


def durationMove(point_x, point_y, duration=0, tween=linear):
    steps = [(point_x, point_y)]

    if duration > MINIMUM_DURATION:
        num_steps = max(abs(point_x), abs(point_y))
        sleep_amount = duration / num_steps
        if sleep_amount < MINIMUM_SLEEP:
            num_steps = int(duration / MINIMUM_SLEEP)
            sleep_amount = int(round(duration * 1000 / num_steps))
            line = RelPointOnLine(point_x, point_y)
            steps = [
                line.getPoint(tween(n / num_steps))
                for n in range(num_steps)
                ]
            steps.append((point_x, point_y))

        if len(steps) > 1:
            prve_x = None
            prve_y = None
            for i in range(len(steps)):
                x = steps[i][0]
                y = steps[i][1]
                if i != 0:
                    tween_x = x - prve_x
                    tween_y = y - prve_y
                    delay.add_delay(sleep_amount)
                    relmouse.add_relmouse(tween_x, tween_y)
                    print(tween_x, tween_y, sleep_amount)
                prve_x = x
                prve_y = y


if __name__ == '__main__':
    from guitar import point

    durationMove(point.Point(100, 100), duration=0.3)
