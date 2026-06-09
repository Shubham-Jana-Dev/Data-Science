#include <Python.h>
/*. cd "/Users/shubhamjana/Data-Science/2026_06_09_(Numpy_slicing)/" && g++ slicing.cpp -I/opt/homebrew/opt
/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14 -F/opt/homebrew/opt/python@3.14/Frameworks -framework Python -o slicing && "/
Users/shubhamjana/Data-Science/2026_06_09_(Numpy_slicing)/"slicing && rm slicing
*/
int main(){
    Py_Initialize();
    const char* pythonCode = R"(
import numpy as np
a = np.array([10,20,40])
print(a.dtype)

b = np.array([10.23,2.34,4.90])
print(b.dtype)

c = np.array(['Shubham','Raj'])
print(c.dtype)
print(c.size)
print(c.itemsize)

x = np.array(["Hello"],dtype = "U3")
print(x)

y = np.array([-128],dtype = np.int8)
print(y)

fl = np.array([12.33,34.5,65.67],dtype = np.int16)
print(fl)

ff = a.astype(float)
print(ff)
print(a)

dd = np.array([10,23,42,3,51,4,6,75,7,98,33,565])
print(dd[:7:2])

print(dd[5:8])

print(dd[2:6])

print(dd[:7:-1])

print(dd[::-1])

arr2d = np.array([[1,2,3,4],
          [4,5,6,8],
          [66,7,55,78],
          [19,29,78,90]])
print(arr2d[:2, 2:])
print(arr2d[::-1,::-1])

er = arr2d.astype(str)
print(er)


)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
return 0;
}