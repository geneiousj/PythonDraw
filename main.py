# My name is Jaskeerat Singh and my student number is 251030244.
import area_calculation
import draw_shapes


def is_valid_shape(in_value: str):
    """
    Function to check if user input entered is valid.
    :param in_value: in_value is a string input to check if the input is one of the strings mentioned in the function.
    :return: returns tru is the value is okay, and false if the value is not one of the pre-decided ones.
    """
    if in_value.lower() not in ('circle', 'triangle', 'square', 'done'):
        return True
    else:
        return True

def main():
    """
    This function handles user input and outputs the area of shapes and a drawing of
the shapes requested.
    :return: will provide the area and drawing of shapes as requested by user.
    """
    area_list = []
    scale = float(8)
    axis_scale = float(0.8)
    shape = input('What shape would you like to draw?\n')
    while is_valid_shape(shape):
        is_valid_shape(shape)
        if shape.lower() == 'circle':
            color = input('What color would you like the shape to be?\n')
            xposition = int(input('What is the x position?\n'))
            yposition = int(input('What is the y position?\n'))
            radius = float(input('What is the radius of the circle?\n'))
            circle_area = float("{:.2f}".format(area_calculation.circle_area(radius)))
            print(f'The calculated area is {circle_area:.2f}.\n')
            draw_shapes.draw_circles(radius*scale, xposition*axis_scale, yposition*axis_scale, color)
            area_list.append(circle_area)
            shape = input('What shape would you like to draw?\n')

        elif shape.lower() == 'triangle':
            color = input('What color would you like the shape to be?\n')
            xposition = float(input('What is the x position?\n'))
            yposition = float(input('What is the y position?\n'))
            base = float(input('What is the length of the base of the triangle ?\n'))
            triangle_area = float("{:.2f}".format(area_calculation.triangle_area(base)))
            print(f'The calculated area is {triangle_area:.2f}.\n')
            area_list.append(triangle_area)
            draw_shapes.draw_triangle(base*scale, xposition*axis_scale, yposition*axis_scale, color)
            shape = input('What shape would you like to draw?\n')

        elif shape.lower() == 'square':
            color = input('What color would you like the shape to be?\n')
            xposition = float(input('What is the x position?\n'))
            yposition = float(input('What is the y position?\n'))
            length = float(input('What is the length of the side of the square ?\n'))
            square_area = float("{:.2f}".format(area_calculation.square_area(length)))
            print(f'The calculated area is {square_area:.2f}.\n')
            area_list.append(square_area)
            draw_shapes.draw_square(length*scale, xposition*axis_scale, yposition*axis_scale, color)
            shape = input('What shape would you like to draw?\n')

        elif shape.lower() == 'done':
            thanks = f'Thanks for using this program! Here is a list of areas that we calculated for you: {area_list}.\n'
            print(thanks)
            break

        elif shape.lower() not in ('circle', 'triangle', 'square', 'done'):
            print('Sorry, but that shape does not exist in our system. Please try again.\n')
            shape = input('What shape would you like to draw?\n')

main()
