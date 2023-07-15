# challenge 1
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))
z = int(input("enter the value of z: "))
point = Point(x, y, z)
result = point.sqSum()
print("Squared Sum:",result)