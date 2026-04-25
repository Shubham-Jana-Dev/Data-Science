// Multi value asignment by using arbitry keyword variable.
#include <Python.h>

int main(){
    Py_Initialize();
    const char* pythonCode = R"(
x, y = 202,342
print(x)
print(y)
a, *b = 23,45,12,66,77,89,45,23
print(a)    
print(b)
g, *f = 55,65,6,23,45,77
print(g)
print(*f)
'''
def wrong_syntax():
    *o = 100,45,3,23,67,98,233 #we can not 
    ee, **h = 56,56,88,98,12,88,90
    *y,*t = 34,55,67,8,90,89
wrong_syntax()
'''
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}