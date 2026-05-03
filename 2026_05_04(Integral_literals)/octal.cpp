#include <Python.h>
int main(){
    Py_Initialize();
    const char* pythonCode = R"(
x = 422347809
print(x)
print(type(x))
y = oct(x)
print(y)
print(type(y))
print("The radix of the octal represent are: 0o and 0O.")
My_octal_number = 0o323476432
print(My_octal_number)
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}