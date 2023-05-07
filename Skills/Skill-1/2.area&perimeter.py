class circle:
    def circle(self,a):
        self.a=a
        print("Circle Area:",3.14*a*a)
        print("Circle Perimeter:",2*3.14*a)
class Square(circle):
    def square(self,a):
        print("Square Area:",a*a)
        print("Square perimeter:",4*a)
class Rectangle(circle):
    def rectangle(self,a,b):
        print("Rectangle Area:",a*b)
        print("Rectangle perimeter:",2*a+2*b)
class Triangle(circle):
    def triangle(self,a,b,c):
        print("Triangle perimeter:",a+b+c)
        s=(a+b+c)/2
        print("Triangle area:", (s * (s - a) * (s - b) * (s - c)) ** 0.5)
obj=Square()
a=int(input())
obj.square(a)
obj.circle(a)
obj=Rectangle()
b=int(input())
obj.rectangle(a,b)
obj=Triangle()
c=int(input())
obj.triangle(a,b,c)


