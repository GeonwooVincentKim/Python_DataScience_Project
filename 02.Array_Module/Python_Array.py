import array
import collections.abc as abc

a = array.array('i', [1, 2, 3, 4, 5])
print(type(a))
print(a)

print(issubclass(type(a), abc.MutableSequence))

print("\n")
# Check the Array-TypeCode and Byte-Size of Element.
print(a.typecode)
print(a.itemsize)

print("\n")
# Check the number of Element and Array-Reference.
print(a.buffer_info())
print(a[0])
print(a[-1])
print(len(a))

try:
    a[5] = 100
except Exception as e:
    print(e)
