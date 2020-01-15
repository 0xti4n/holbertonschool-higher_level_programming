#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(4, 2)
print(my_rectangle.width)

my_rectangle.width =  3
my_rectangle.height = 10
print(my_rectangle.__dict__)
