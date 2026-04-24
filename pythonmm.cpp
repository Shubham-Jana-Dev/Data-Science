#include <Python.h>

int main(){
    Py_Initialize();
    const char* pythonCode = R"(
print("Hello Shubham")
    
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}