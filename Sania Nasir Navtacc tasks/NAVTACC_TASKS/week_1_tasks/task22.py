# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "dog"
# tuple unpacking is also possible
a, b, c = my_tuple

>>> my_tuple = ("hello")   # only parentheses is not enough
>>> type(my_tuple)
<class 'str'>
>>> my_tuple = ("hello",)  # need a comma at the end
>>> type(my_tuple)
<class 'tuple'>
>>> my_tuple = "hello",    # parentheses is optional
>>> type(my_tuple)
<class 'tuple'>

>>> my_tuple = ['p','e','r','m','i','t']
>>> my_tuple[0]
'p'
>>> my_tuple[5]
't'
>>> my_tuple[6]   # index must be in range
...
IndexError: list index out of range
>>> my_tuple[2.0] # index must be an integer
...
TypeError: list indices must be integers, not float
>>> n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
>>> n_tuple[0][3]  # nested index
's'
>>> n_tuple[1][1]  # nested index
4
>>> n_tuple[2][0]  # nested index
1

>>> my_tuple = ['p','e','r','m','i','t']
>>> my_tuple[-1]
't'
>>> my_tuple[-6]
'p'

>>> my_tuple = ('p','r','o','g','r','a','m','i','z')
>>> my_tuple[1:4]  # elements 2nd to 4th
('r', 'o', 'g')
>>> my_tuple[:-7]  # elements beginning to 2nd
('p', 'r')
>>> my_tuple[7:]   # elements 8th to end
('i', 'z')
>>> my_tuple[:]    # elements beginning to end
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

*---*---*---*---*---*---*---*---*---*
 | p | r | o | g | r | a | m | i | z |
 *---*---*---*---*---*---*---*---*---*
 0   1   2   3   4   5   6   7   8   9
-9  -8  -7  -6  -5  -4  -3  -2  -1

>>> my_tuple = (4, 2, 3, [6, 5])
>>> my_tuple[1] = 9  # we cannot change an element
...
TypeError: 'tuple' object does not support item assignment
>>> my_tuple[3] = 9  # we cannot change an element
...
TypeError: 'tuple' object does not support item assignment
>>> my_tuple[3][0] = 9   # but item of mutable element can be changed
>>> my_tuple
(4, 2, 3, [9, 5])
>>> my_tuple = ('p','r','o','g','r','a','m','i','z') # tuples can be reassigned
>>> my_tuple
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

>>> (1, 2, 3) + (4, 5, 6)
(1, 2, 3, 4, 5, 6)
>>> ("Repeat",) * 3
('Repeat', 'Repeat', 'Repeat')

>>> my_tuple = ('p','r','o','g','r','a','m','i','z')
>>> del my_tuple[3] # can't delete items
...
TypeError: 'tuple' object doesn't support item deletion
>>> del my_tuple    # can delete entire tuple
>>> my_tuple
...
NameError: name 'my_tuple' is not defined

>>> my_tuple = ('a','p','p','l','e',)
>>> my_tuple.count('p')
2
>>> my_tuple.index('l')
3

>>> my_tuple = ('a','p','p','l','e',)
>>> 'a' in my_tuple
True
>>> 'b' in my_tuple
False
>>> 'g' not in my_tuple
True

>>> for name in ('John','Kate'):
...     print("Hello",name)
...     
Hello John
Hello Kate

