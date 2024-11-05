class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length  # square
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

square = Rectangle(5)
rectangle = Rectangle(5, 3)
print("Square area:", square.area())
print("Rectangle area:", rectangle.area())
