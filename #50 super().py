# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")



class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

#we don't need to manually assign these attributes
# self.color = color
# self.is_filled = is_filled
# within each of these constructors for the children

#instead what we have to do is within the constructor for each of these children classes
#we have to call constructor for the parent also known as the super class of shape

#we're going to call the super function to take care of whatever attributes all these types of shapes have in common such as 'common' and 'is_filled'

circle = Circle("red", True, 5)
square = Square(color="blue", is_filled=True, width=6)
triangle = Triangle("yellow", True, 7, 8)



print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")


print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")


circle.describe()
square.describe()
triangle.describe()

#METHOD OVERWRITING
#what if we create a similar method of describe within circle square and triangle

#if a child shares a similar method with a parent you'll use the child's version and not the parents

#not only do I want to use the describe method of the child I would also like to use the describe method of the parent

