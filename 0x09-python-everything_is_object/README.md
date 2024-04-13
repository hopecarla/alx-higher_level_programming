0x09. Python - Everything is object
Work on the following is done below:

Learning Objectives At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General Why Python programming is awesome What is an object What is the difference between a class and an object or instance What is the difference between immutable object and mutable object What is a reference What is an assignment What is an alias How to know if two variables are identical How to know if two variables are linked to the same object How to display the variable identifier (which is the memory address in the CPython implementation) What is mutable and immutable What are the built-in mutable types What are the built-in immutable types How does Python pass variables to functions

Who am I? mandatory What function would you use to get the type of an object?
Write the name of the function in the file, without ().

Where are you? mandatory How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().

Right count mandatory In the following code, do a and b point to the same object? Answer with Yes or No.
a = 89 b = 100

Right count = mandatory In the following code, do a and b point to the same object? Answer with Yes or No.
a = 89 b = 89

Right count = mandatory In the following code, do a and b point to the same object? Answer with Yes or No.
a = 89 b = a

Right count =+ mandatory In the following code, do a and b point to the same object? Answer with Yes or No.
a = 89 b = a + 1

Is equal mandatory What do these 3 lines print?
s1 = "Best School" s2 = s1 print(s1 == s2)

Is the same mandatory What do these 3 lines print?
s1 = "Best" s2 = s1 print(s1 is s2)

Is really equal mandatory What do these 3 lines print?
s1 = "Best School" s2 = "Best School" print(s1 == s2)

Is really the same mandatory What do these 3 lines print?
s1 = "Best School" s2 = "Best School" print(s1 is s2)

And with a list, is it equal mandatory What do these 3 lines print?
l1 = [1, 2, 3] l2 = [1, 2, 3] print(l1 == l2)

And with a list, is it the same mandatory What do these 3 lines print?
l1 = [1, 2, 3] l2 = [1, 2, 3] print(l1 is l2)

And with a list, is it really equal mandatory What do these 3 lines print?
l1 = [1, 2, 3] l2 = l1 print(l1 == l2)

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

a = ()
Is a a tuple? Answer with Yes or No.

a = (1, 2)
Is a a tuple? Answer with Yes or No.

a = (1)
Is a a tuple? Answer with Yes or No.

a = (1, )
Is a a tuple? Answer with Yes or No.

What does this script print?

a = (1)
b = (1)
a is b

What does this script print?

a = (1, 2)
b = (1, 2)
a is b

What does this script print?

a = ()
b = ()
a is b

>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
