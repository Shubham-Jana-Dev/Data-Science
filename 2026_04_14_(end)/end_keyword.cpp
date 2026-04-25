//Demonstrait about end=" "
//By the help of end=" " function we can manage the space area
// of main thred.
//means we can print the statement having multiple statement.
#include <Python.h>

int main(){
    Py_Initialize();
    const char* pythonCode = R"(
print("Hello Shubham")    
print("Hi",end=" ")
print("Shubham",end=" ")
print("\n--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--\n")
print("I",end="_")
print("love",end="_")
print("to",end="_")
print("code",end="_")
print("Python",end="_")
print("code",end="_")
print("in",end="_")
print("C++",end="_")
print("file.")
print("\n--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--\n")
print("Hi",end="$")
print("Rahul",end="@")
print("\n--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--\n")
x = 60
y = 56
z = 70
print(x,y,z,end="%")
print("\n--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--^v^--\n")
t,y,u = 43,55,98
print(t,y,u,sep="-")
print(x,y,z,sep="%")
)";
PyRun_SimpleString(pythonCode);
Py_Finalize();
}