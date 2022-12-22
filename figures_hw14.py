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

    def draw(self) -> None:
        for _ in range(1, self.width):
            print(_ * '*')


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self) -> None:
        print(('*' * self.width + '\n') * self.height)


figures = [Rectangle(10, 10), Triangle(2)]

for i in figures:
    print(i.draw())






