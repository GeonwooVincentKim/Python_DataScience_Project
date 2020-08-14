import numpy as np
import collections.abc as abc

print(np.__version__)

a = np.array([1, 2, 3, 4])
print(a)

issubclass(type(a), abc.MutableSequence)
# Applied MutableSequence, an Abstracted-Class
# and check for Method that we must implement
# the code.
abc.MutableSequence.__abstractmethods__
dir(np.ndarray).count('insert')

print(a.dtype)
print(a.ndim, a.shape, a.itemsize)

print("\n")
print(a.strides)
print(a.data, a.data.obj, a.tolist())

print("\n")
d = np.dtype(np.int32)
print(d)
print(type(d))
print(d.char, d.kind, d.itemsize)

dt = np.dtype("<i4")
print(dt.byteorder)
print(a.tobytes)

print("\n")

# Reverse the sign of inequality
# to create a data type.
dt1 = np.dtype(">i4")
print(dt1.byteorder)
