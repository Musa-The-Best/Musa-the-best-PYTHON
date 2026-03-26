class Polygon:
    def area(self): pass
    def perimeter(self): pass

class Square(Polygon):
    def __init__(self,s): self.s=s
    def area(self): return self.s**2
    def perimeter(self): return 4*self.s

class Rectangle(Polygon):
    def __init__(self,l,w): self.l=l; self.w=w
    def area(self): return self.l*self.w
    def perimeter(self): return 2*(self.l+self.w)

class Triangle(Polygon):
    def __init__(self,b,h,s1,s2,s3): self.b=b; self.h=h; self.s1=s1; self.s2=s2; self.s3=s3
    def area(self): return 0.5*self.b*self.h
    def perimeter(self): return self.s1+self.s2+self.s3

shapes=[Square(5),Rectangle(4,6),Triangle(4,3,4,3,5)]
for sh in shapes: print(f"{sh.__class__.__name__}: Area={sh.area()} Perimeter={sh.perimeter()}")