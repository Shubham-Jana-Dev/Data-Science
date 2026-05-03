#include <Python.h>
int main(){
    Py_Initialize();
    const char* pythonCode = R"(
x = 100
y = '100'
print(f"[id(x) == id(int(y))] ==> {id(x) == id(int(y))}")
print(x*y)
print(f'[id(x) is id(y)] ==> {id(x) is id(y)}')
print(f"[id(x) is id(int(y))] ==> {id(x) is id(int(y))}")
print(f'type([id(x) == type(id(int(y)))] ==> {id(x) == type(id(int(y)))}')
a,*b,z = 12,2,1,43,53,76,87,90
print(a)
print(b) # *b return the list
print(z)
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}