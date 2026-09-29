class Point:
    __slots__ = ("x", "y")
    def __init__(self,x,y): self.x=x; self.y=y
print(Point(1,2).x)