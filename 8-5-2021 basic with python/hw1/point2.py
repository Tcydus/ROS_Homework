from math import sqrt

class Point2:
    def __init__(self,x,y) -> None:
        self._x = x
        self._y = y

    def get_distance(self,other):
        return sqrt(pow(self._x - other._x,2) + pow(self._y - other._y,2))

    def __add__(self,other):
        return Point2(self._x + other._x,self._y + other._y)
    
    def __sub__(self,other):
        return Point2(self._x - other._x,self._y - other._y)
    
    def __str__(self) -> str:
        return "Position (x,y) : (" + str(self._x) + "," +str(self._y) + ")"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value 

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        self._y = value 

if __name__ == "__main__" :
    obj1 = Point2(5,10)
    obj2 = Point2(2,6)
    print(obj1)
    print(obj2)
    print("distance : ",obj2.get_distance(obj1))
