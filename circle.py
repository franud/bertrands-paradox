import random
import math


# This class is used for creating a random point {(x,y) | x² + y² = 1}, that meaning that is a random point that belongs to the unit circle
class PointInACircle:
    #If x and y argument are passed, the point is the one at (x,y), but it doesn't have to belong to the circle exception is raised
    def __init__ (self, x = None, y = None):
        if x == None and y == None:
            self.x = random.uniform(-1,1)
            self.y = PointInACircle.generate_valid_point (self.x)
        else:
            if PointInACircle.is_valid_point(x,y):
                self.x = x
                self.y = y
            else:
                raise NameError("Point doesn't belong to the unit circle")
            

    def __str__ (self):
        return '(%s,%s)' % (self.x, self.y)
    

    def is_valid_point (x,y):
        sum = pow (x,2) + pow (y,2)
        return sum == 1

    #generates a valid coordinate of a point that belongs to the unit circle knowing one coordinate of it
    def generate_valid_point (x):
        sign = random.randint(0,1)
        if sign == 0:
            return -1 * (math.sqrt(1 - math.pow(x,2)))
        else: 
            return math.sqrt(1 - math.pow(x,2))

    def distance_to_point (self, p2):
        return ( math.sqrt( math.pow(p2.x - self.x,2) + math.pow (p2.y - self.y, 2) ) )

TRIANGLE_SIDE_LENGHT = math.cos(math.pi/6) * 2

arc_bigger_than_triangle_side = 0
n = int (input ("Insert number of operations: "))

for i in range(n):
    p1 = PointInACircle()
    p2 = PointInACircle()
    if p1.distance_to_point(p2) > TRIANGLE_SIDE_LENGHT:
        arc_bigger_than_triangle_side += 1

print (arc_bigger_than_triangle_side, n, arc_bigger_than_triangle_side/n)