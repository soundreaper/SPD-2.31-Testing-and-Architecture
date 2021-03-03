# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, circle):
        return math.sqrt((self.x - circle.x)**2 + (self.y - circle.y)**2)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self, vector):
        return math.sqrt((self.x-vector.y)*(self.x-vector.x) + (self.y-vector.y)*(self.y-vector.y))


# calculate the distance between the two circle
circle1 = Circle(4, 4.25)
circle2 = Circle(53, -5.35)

distance = circle1.distance(circle2)
print(distance)

# calculate the length of vector AB vector which is a vector between A and B points
vector1 = Vector(-36, 97)
vector2 = Vector(.34, .91)

length = vector1.length(vector2)
print(length)
