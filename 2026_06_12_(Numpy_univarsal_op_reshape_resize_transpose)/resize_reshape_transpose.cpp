#include <Python.h>

int main(){
    Py_Initialize();
    const char* pythonCode = R"(
# Universal operator
import numpy as np
print(np.add(2,3))
print(np.subtract(5,6))
print(np.multiply(2,9))
print(np.divide(8,2))
print(np.floor_divide(77.4,5.77))
a = np.array([1.9,2.54,6.1,4.5,5.9])
print(np.max(a))
print(np.min(a))
print(np.square(5))
print(np.sqrt(25))
print(np.abs(-9.7))
print(np.abs(7.9))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.mod(3,5))
print(np.power(a,3))

b = np.floor(a)
print(b.dtype)

# .reshape() 
x = np.array([[12,33,45,67],
              [32,55,76,89],
              [16,17,19,90]])
print(np.shape(x))
y = x.reshape(2,6)
print(y)

arr = np.arange(0,12)
print(arr)
print(arr.reshape(3,4))

print(np.resize(arr,[2,6]))

bb = arr.reshape(3,4)
arree = arr.transpose()
print(bb.T)

print(np.expand_dims(bb,axis = 1))

print(np.squeeze(bb))
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}