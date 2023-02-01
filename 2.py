from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print (rect_1.get_area())
print (rect_2.get_area())

square_1 = Square(5)
square_2 = Square(15)

print(square_1.get_area_square(), square_2.get_area_square())

circle_1 = Circle(4)
circle_2 = Circle(12)

print(circle_1.get_area_circle(), circle_2.get_area_circle())
