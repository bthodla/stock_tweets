import turtle
import math
import time

def polyline(t: turtle, sides: int, length: int, angle: int):
    """Draws *sides* line segments with the given length and angle (in degrees) between them
    :param t: turtle
    :param sides: 
    :param length: 
    :param angle: 
    :return: 
    """
    for i in range(sides):
        t.fd(length)
        t.lt(angle)


def polygon(t: turtle, sides: int, length: int):
    angle = 360 / sides
    polyline(t, sides, length, angle)
    time.sleep(1)


def square(t: turtle, length: int):
    polygon(t, 4, length)


def triangle(t: turtle, length: int):
    polygon(t, 3, length)


def arc(t: turtle, radius: int, angle: int):
    arc_length = 2 * math.pi * radius * angle / 360
    sides = int (arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = float (angle) / sides
    polyline(t, sides, step_length, step_angle)


def circle(t: turtle, radius: int):
    angle = 360
    arc(t, radius, angle)


