Learning Objectives At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General Why Python programming is awesome What is a superclass, baseclass or parentclass What is a subclass How to list all attributes and methods of a class or instance When can an instance have new attributes How to inherit class from another How to define a class with multiple base classes What is the default class every class inherit from How to override a method or attribute inherited from the base class Which attributes or methods are available by heritage to subclasses What is the purpose of inheritance What are, when and how to use isinstance, issubclass, type and super built-in functions

Lookup Write a function that returns the list of available attributes and methods of an object:
Prototype: def lookup(obj): Returns a list object You are not allowed to import any module

My list Write a class MyList that inherits from list: Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort) You can assume that all the elements of the list will be of type int You are not allowed to import any module

Exact same object Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class): You are not allowed to import any module

Same class or inherit from Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False. Prototype: def is_kind_of_class(obj, a_class): You are not allowed to import any module

Only sub class of Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False. Prototype: def inherits_from(obj, a_class): You are not allowed to import any module

Geometry module Write an empty class BaseGeometry. You are not allowed to import any module

Improve Geometry Write a class BaseGeometry (based on 5-base_geometry.py). Public instance method: def area(self): that raises an Exception with the message area() is not implemented You are not allowed to import any module

Integer validator Write a class BaseGeometry (based on 6-base_geometry.py). Public instance method: def area(self): that raises an Exception with the message area() is not implemented Public instance method: def integer_validator(self, name, value): that validates value: you can assume name is always a string if value is not an integer: raise a TypeError exception, with the message must be an integer if value is less or equal to 0: raise a ValueError exception with the message must be greater than 0 You are not allowed to import any module

Rectangle Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Instantiation with width and height: def init(self, width, height): width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator

Full rectangle Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py) Instantiation with width and height: def init(self, width, height):: width and height must be private. No getter or setter width and height must be positive integers validated by integer_validator the area() method must be implemented print() should print, and str() should return, the following rectangle description: [Rectangle] /

Square #1 Write a class Square that inherits from Rectangle (9-rectangle.py): Instantiation with size: def init(self, size):: size must be private. No getter or setter size must be a positive integer, validated by integer_validator the area() method must be implemented

Square #2 Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py). Instantiation with size: def init(self, size):: size must be private. No getter or setter size must be a positive integer, validated by integer_validator the area() method must be implemented print() should print, and str() should return, the square description: [Square] /
