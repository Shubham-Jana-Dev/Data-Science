#include <iostream>
#include <Python.h>
class numpy{
public:
void show_numpy_version(){
    Py_Initialize();
    const char* pythonCode = R"(
import numpy as np
class NumpyVersion:
    def show_version():
        print(np.__version__)
n1 =  NumpyVersion
n1.show_version()
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}
};
int main(){
    numpy snv;
    snv.show_numpy_version();
    return 0;
}
