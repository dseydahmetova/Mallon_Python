import math
class Point:
    @classmethod
    def origin(cls):
        return cls(0, 0)
    @classmethod
    def left(cls):
        return cls(-1, 0)
    @classmethod
    def right(cls):
        return cls(1, 0)

    @classmethod
    def up(cls):
        return cls(0, 1)

    @classmethod
    def down(cls):
        return cls(0, -1)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # move right
    def __rshift__(self, other):
        return Point(self.x + other.x, self.y)

    # move left
    def __lshift__(self, other):
        return Point(self.x - other.x, self.y)

    # move up
    def __add__(self, other):
        return Point(self.x, self.y + other.y)

    # move down
    def __sub__(self, other):
        return Point(self.x, self.y - other.y)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return "Both are equal"
        else:
            return "Not equal"

    def distance(self, other):
        return round(math.dist((self.x, self.y ), (other.x, other.y)))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# point1
point1 = Point(2, 3)

# point2
point2 = Point(5, 1)

print("Point1:", point1)
print("Point2:", point2)

moveRight = point1 >> point2
print("Moved right:", moveRight)

moveLeft = point1 << point2
print("Moved left:", moveLeft)

moveUp = point1 + point2
print("Moved up:", moveUp)

moveDown = point1 - point2
print("Moved down:", moveDown)


print("Comparison: ", point1 == point2)

print("Distance: ", point1.distance(point2))