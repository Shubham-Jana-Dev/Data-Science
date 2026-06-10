#include <Python.h>
int main(){
    Py_Initialize();
    const char* pythonCode = R"(
import numpy as np
arr = np.array([12,32,45,66])
print(arr)

# 2D array:
arr2d = np.array([['add','b','c'],['d','ettr','f']])
print(arr2d)

# 3D array:
arr3d = np.array([[[1,2,3,4],[2,3,54,67],[11,54,76,89]],
                  [[12,44,65,78],[65,67,87,33],[23,45,12,13]],
                  [[30,54,21,43],[543,67,80,81],[122,554,789,10]]])
print(arr3d)

# One's array:
print(np.ones(5))
# 2d ones array:
print(np.ones((2,3)))
# 3d ones array:
print(np.ones((3,3)))

# Zero's array:
print(np.zeros(5))
# 2d zeros array:
print(np.zeros((2,3)))
# 3d zeros array:
print(np.zeros((3,3)))

# Empty array:
print(np.empty(3))
# 2d empty array:
emp2d = np.empty((2,3))
print(emp2d)
# 3d empty array:
emp3d = np.empty((3,4))
print(emp3d)

# .shape function ==> Showes the number of rows and columns.
print(arr.shape)
print(arr2d.shape)
print(arr3d.shape)

# .size function ==> total elements of an array.
print(arr.size)
print(arr2d.size)
print(arr3d.size)

# .ndim function ==> the number of dimention.
print(arr.ndim)
print(arr2d.ndim)
print(arr3d.ndim)

# .dtype function ==> shows the data type of the elements in an array.
print(arr.dtype)
print(arr2d.dtype)
rr = np.array([[2.3,4.5,5.6],[2.4,3.5,7.9]])
print(rr.dtype)

# .itemsize ==> Memory (in bytes) used by each element.
print(arr.itemsize)
print(arr2d.itemsize)
print(rr.itemsize)

# .nbytes function ==> Total memory used by the array.
print(arr.nbytes)
print(arr2d.nbytes)
print(rr.nbytes)

er = np.linspace(0,10,5)
print(er)
)";
    PyRun_SimpleString(pythonCode);
    Py_Finalize();
}