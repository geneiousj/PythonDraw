# My name is Jaskeerat Singh and my student number is 251030244.
import math

def circle_area(radius: int):
    """
This function calculates the area of a circle.
    :param radius: radius of the circle for which area must be calculated.
    :return:the area of a circle
    """
    area = math.pi * radius ** 2
    return area

def square_area(length):
    """
    This function calculates the area of a square.
    :param length: length of square's side
    :return: the area of a square.
    """
    area = length ** 2
    return area

def triangle_area(base):
    """
    This function calculates the area of a triangle.
    :param base: the length of the triangle's base
    :return: the area of the equilateral triangle
    """
    area = (math.sqrt(3)/4) * base ** 2
    return area

