# Create a super class Shape and its descendants Triangle, Rectangle.
# The Shape class contains an abstract draw method
# The Triangle class in the initializer takes the width parameter: int - the width of the triangle and
# implements the draw method
# (Displays a triangle with width in the console)
# The Rectangle class in the initializer takes the parameter width: int and height: int - the width,
# height of the rectangle and implements the draw method (Displays a rectangle with width and height to the console)
# Create a list with these shapes and call the draw method on these objects in a loop


class Shape:

    def draw(self) -> None:
        pass


class Triangle(Shape):

    def __init__(self, width: int):
        self.width = width

    def draw(self) -> str:
        for i in range(self.width):
            for j in range(i + 1):
                print('* ', end='')
            print()
        return f'Triangle was drawn with a width - {self.width}'


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self) -> str:
        for i in range(self.height):
            for j in range(self.width):
                print('* ', end='')
            print()
        return f'Rectangle was drawn with a width - {self.width} and a height - {self.height}'


figures = [
    Triangle(7),
    Rectangle(6, 10),
]

for figure in figures:
    print(figure.draw())









