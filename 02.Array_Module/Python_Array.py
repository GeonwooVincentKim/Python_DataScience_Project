import array
import collections.abc as abc

a = array.array('i', [1, 2, 3, 4, 5])
print(type(a))
print(a)

print(issubclass(type(a), abc.MutableSequence))