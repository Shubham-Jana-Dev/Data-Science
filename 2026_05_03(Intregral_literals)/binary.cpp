#include <Python.h>
int main(){
    Py_Initialize();
    const char* pythonCode = R"(
x = 5993
print(x)
print(type(x))   #it should retun 'int'.
y = bin(x)       #we use bin() to get the binary represention of any decimal value.
print(y)         #it would return the binary represention of the x.
print(type(y))   #it would return 'str' because of the 0b (prefix).
My_binary_number = 0b11101101011001   #by using 0b prefix we tell PVM that it's a binary number not a integer number. 
print(My_binary_number)               #If we try to print the binary number directly, it would retun the corespondig decimal vaule.
)";
    PyRun_SimpleString(pythonCode);
    Py_Finalize();
}