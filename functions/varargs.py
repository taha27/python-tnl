'''Let's play with the different ways to use variable arguments in
Python.  Define the functions below to make everything pass.

>>> values = {"a":3, "b":2, "c":4}
>>> some_values = {"c": 7, "b": 4}

>>> product(2, 7, 3)
42
>>> product(**values)
24
>>> product(1, **some_values)
28

>>> amounts = {"u": 3, "v": 2, "w": 4}
>>> some_amounts = {"v": 7, "w": 4}
>>> total(1, 2, 3)
6
>>> total(**amounts)
9
>>> total(3, **some_amounts)
14

>>> max_even(2, 3)
2
>>> max_even(2, 4)
4
>>> max_even(2, 3, 9, 11, 7, 8, 13, 21)
8


>>> point = (3, 8, 2)
>>> coordinates = {'x': 8, 'y': 33, 'z': -4}

IMPORANT HINT: Remember that * and ** are used for two different
things: when _calling_ a function (argument unpacking), and when
_defining_ a function (varargs).

>>> set_destination(*point)
Going to x=3, y=8, z=2

>>> set_destination(**coordinates)
Going to x=8, y=33, z=-4

'''

# Write your code here:


def set_destination(x, y, z):
    print(f"Going to x={x}, y={y}, z={z}")


def product(a, b, c):
    print(a * b * c)


def total(u, v, w):
    print(u + v + w)


def max_even(*args):
    if not args:
        print(None)
    max_even = args[0]
    for arg in args[1:]:
        if arg % 2 == 0 and arg > max_even:
            max_even = arg
    print(max_even)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
