"""
    Apply Abstract-Class that includes Data-Structure System.
"""
import collections.abc as abc

# Check Abstract-Methods that implemented
# in the Sequence-Class.
abc.Sequence.__abstractmethods__

# Check Abstract-Methods of MMutable-Sequence-Class.
abc.MutableSequence.__abstractmethods__

# Check the Relationship of Inheritance
# between List-Class and Sequence-Class.
issubclass(list, abc.Sequence)

# Check the Relationship of Inheritance
# between List-Class and Mutable-Sequence-Class.
issubclass(list, abc.MutableSequence)

x = list((1, 2, 3, 'a'))
print(x)

# Creation
isinstance(x, list)
print(x[0], x[-1])

try:
    print(x[10])
except Exception as e:
    print(e)
