
import turtle


def prepare_to_draw(position_x,position_y,colour):
    """
    This function handles the position of the pen on the canvas as well as its colour.
    :param position_x:  the x position to start drawing at
    :param position_y: the y position to start drawing at
    :param colour: the colour to fill the shape with
    """
    turtle.penup()
    turtle.goto(position_x, position_y)
    turtle.pendown()
    turtle.fillcolor(colour)
    turtle.begin_fill()

def draw_circles(radius, position_x, position_y, colour):
    """
    This function can be used to draw circles using the turtle module.
    :param radius: input for the radius of th desired circle.
    :param position_x:  the x position to start drawing at.
    :param position_y: the y position to start drawing at.
    :param colour: the colour to fill the shape with.
    """
    prepare_to_draw(position_x,position_y,colour)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


def draw_square(length, position_x, position_y, colour):
    """
    This function can be used to draw squares using the turtle module.
    :param length: input for the length of the side of the desired square.
    :param position_x:  the x position to start drawing at.
    :param position_y: the y position to start drawing at.
    :param colour: the colour to fill the shape with.
    """
    prepare_to_draw(position_x, position_y, colour)
    turtle.fd(length)
    turtle.lt(90)
    turtle.fd(length)
    turtle.lt(90)
    turtle.fd(length)
    turtle.lt(90)
    turtle.fd(length)
    turtle.lt(90)
    turtle.end_fill()
    turtle.penup()


def draw_triangle(base, position_x, position_y, colour):
    """
    This function can be used to draw triangles using the turtle module.
    :param base: input for th lngth of the base of the triangle.
    :param position_x:  the x position to start drawing at.
    :param position_y: the y position to start drawing at.
    :param colour: the colour to fill the shape with.
    """
    prepare_to_draw(position_x, position_y, colour)
    turtle.fd(base)
    turtle.lt(120)
    turtle.fd(base)
    turtle.lt(120)
    turtle.fd(base)
    turtle.lt(120)
    turtle.end_fill()
    turtle.penup()


