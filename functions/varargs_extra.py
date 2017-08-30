'''

Let's write a couple of trickier functions, which scan through
passed-in keyword arguments.

>>> country_populations = {
...     "Russia": 144,
...     "USA": 319,
...     "Philippines": 99,
...     "India": 1252,
... }

>>> val_for_longest_key(a=1)
1
>>> val_for_longest_key(a=2, aa=3)
3
>>> val_for_longest_key(foo=10, alpha=3, x=9)
3
>>> val_for_longest_key(**country_populations)
99

>>> key_for_biggest_value(a=1)
'a'
>>> key_for_biggest_value(a=2, aa=3)
'aa'
>>> key_for_biggest_value(foo=10, alpha=3, x=9)
'foo'
>>> key_for_biggest_value(**country_populations)
'India'

'''

# Write your code here:


def key_for_biggest_value(**kwargs):
    key_for_val = None
    max_val = 0
    for key, val in kwargs.items():
        if val > max_val:
            max_val = val
            key_for_val = key
    return key_for_val


def val_for_longest_key(**kwargs):
    max_key = ''
    val_for_key = None
    for key, val in kwargs.items():
        if len(key) > len(max_key):
            max_key = key
            val_for_key = val
    return val_for_key


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
