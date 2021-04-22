
class EPoint:
    def __init__(self, a = 0, b = 1, c = 0):
        self.x = a
        self.y = b
        self.z = c
    
    def __eq__(self, T):
        return self.x == T.x and self.y == T.y and self.z == T.z

    def __neg__(self):
        return EPoint(self.x, -self.y, self.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)