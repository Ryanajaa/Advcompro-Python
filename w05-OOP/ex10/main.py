from shapes.geometry import Circle, Rectangle

circle = Circle(radius = 10)
rectangle = Rectangle(width = 3, height = 4)

print(f"\nRadius of the circle: {circle.radius}")
print(f"Circle area: {circle.area()}")
print(f"\nWidth, Height of the rectangle: {rectangle.width}, {rectangle.height}")
print(f"Rectangle area: {rectangle.area()}")
