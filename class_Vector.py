
class Vector(object):
    
    def __init__(self, lis):
        self.coords = lis

    def length(self):
        return sum([x**2 for x in self.coords])**.5

    def __add__(self, other):
        return Vector(list(map(lambda x, y: x+y, self.coords, other.coords)))

    def __str__(self):
        return 'Vector'+str(self.coords)
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __mul__(self, other):
        return sum(x*y for x,y in zip(self.coords, other.coords))