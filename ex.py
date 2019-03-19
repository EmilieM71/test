class Vector2(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    @staticmethod
    def from_points(P1, P2):
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude


class Vector2(tuple):

    def __new__(typ, x=1.0, y=1.0):
        n = tuple.__new__(typ, (int(x), int(y)))
        n.x = x
        n.y = y
        return n

    def __mul__(self, other):
        return self.__new__(type(self), self.x*other, self.y*other)

    def __add__(self, other):
        return self.__new__(type(self), self.x+other.x, self.y+other.y)

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    @staticmethod
    def from_points(P1, P2):
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
