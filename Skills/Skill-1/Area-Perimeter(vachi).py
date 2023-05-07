import math
class perimeter:
    def RectanglePerimeter(self,l,b):
        print("Perimeter of Rectangle \t:",2*(l+b))
    def CirclePerimeter(self,r):
        print("Perimeter of Circle \t:%d"%(3.14*2*r))
    def TrianglePerimeter(self,a,b,c):
        print("Perimeter of Triangle \t:%d"%((a+b+c)/3))
class Area(perimeter):
    def RectangleArea(self,l,b):
        super().RectanglePerimeter(l,b)
        print("Area of Rectangle \t:",l*b)
    def CircleArea(self,r):
        super().CirclePerimeter(r)
        print("Area of Circle \t:%d"%(3.14*r*r))
    def TriangleArea(self,a,b,c):
        super().TrianglePerimeter(a,b,c)
        v=(a+b+c)/2
        print("Area of Triangle \t:%d"%(math.sqrt(v*(v-a)*(v-b)*(v-c))))
h=Area()
l=int(input())
b=int(input())
h.RectangleArea(l,b)
r=int(input())
h.CircleArea(r)
a = int(input())
b = int(input())
c = int(input())
h.TriangleArea(a,b,c)