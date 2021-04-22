
from BinaryField.Polynomial import Polynomial as PL

class EPoint:
    def __init__(self, a = PL(), b = PL(1), c = PL()):
        self.x = a
        self.y = b
        self.z = c
    
    def __eq__(self, T):
        return self.x == T.x and self.y == T.y and self.z == T.z

    def __neg__(self):
        return EPoint(self.x, self.x + self.y, self.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)