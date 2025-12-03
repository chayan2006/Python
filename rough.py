
# from abc import ABC, abstractmethod

# # Base Shape Class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def name(self):
#         pass

# # Concrete Shape Classes
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def name(self):
#         return f"Circle (r={self.radius})"

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def name(self):
#         return f"Rectangle (w={self.width}, h={self.height})"

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def name(self):
#         return f"Square (s={self.side})"

# # Shape Machine System
# def shape_machine():
#     shapes = []
    
#     print("Welcome to the Shape Machine Input System!")
#     print("Available shapes: circle, rectangle, square")
#     print("Type 'done' or 'exit' to finish.")

#     while True:
#         try:
#             user_input = input("\nEnter shape type: ").strip().lower()

#             if user_input in ['done', 'exit']:
#                 break

#             new_shape = None
#             if user_input == 'circle':
#                 r = float(input("  Enter radius: "))
#                 new_shape = Circle(r)

#             elif user_input == 'rectangle':
#                 w = float(input("  Enter width: "))
#                 h = float(input("  Enter height: "))
#                 new_shape = Rectangle(w, h)

#             elif user_input == 'square':
#                 s = float(input("  Enter side length: "))
#                 new_shape = Square(s)

#             else:
#                 print("  [!] Invalid shape type. Please try again.")
#                 continue
            
#             if new_shape:
#                 shapes.append(new_shape)
#                 print(f"  -> {new_shape.name()} added.")
                
#                 # Process all shapes in the list (Cumulative "Ans All")
#                 print("\n--- Current Shape Report ---")
#                 for shape in shapes:
#                     print(f"Processing {shape.name()}: Area = {shape.area():.2f}")
#                 print("----------------------------")

#         except ValueError:
#             print("  [!] Invalid input. Please enter numeric values for dimensions.")
    
#     print("--- Shape Machine Session Ended ---")

# if __name__ == "__main__":
#     shape_machine()

class Shape:
    def area(self):
        pass
    