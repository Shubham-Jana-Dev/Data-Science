#include <Python.h>
/* cd "/Users/shubhamjana/Data
-Science/2026_06_10_(Numpy_Negative_indexing_&_Boolean_indexing_&_Fancy_indexing_numpy_operation)/" && g++ numpy_indexing_and_operations.cpp -I/opt/hom
ebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14 -F/opt/homebrew/opt/python@3.14/Frameworks -framework Python -o nump
y_indexing_and_operations && "/Users/shubhamjana/Data-Science/2026_06_10_(Numpy_Negative_indexing_&_Boolean_indexing_&_Fancy_indexing_numpy_operation)/
"numpy_indexing_and_operations && rm numpy_indexing_and_operations
*/
int main(){
    Py_Initialize();
    const char* pythonCode =R"(
import numpy as np
arr1d = np.array([23,44,56,12]);

arr2d = np.array([[12,20,30],
                [40,50,60],
                [80,90,100]]);

arr3d = np.array([[[22,23,45],[13,26,77],[11,89,90]],
                [[12,78,23],[23,44,78],[35,67,89]]]);

print(arr1d[-1]);
print(arr1d[-2]);

print(arr2d[-1]);
print(arr2d[-1,-1]);
print(arr2d[[-1],[-1]]);

print(arr3d[-1,-2,-1]);
print(arr3d[-1]);
print(arr3d[1:3:])

# Boolean indexing:

marks = np.array([60,90,70,80,89,99]);
score = marks>70
print(score)

print([arr3d>40])

# Fancy Indexing:

index_list = [1,4,3,5]

print(marks[index_list])

index_list2 = [1,0,2]
print(arr2d[index_list2])

# NUMPY OPERATION: 

x = np.array([10,20,30,40])
y = np.array(['2','3','4','5'], dtype=np.int32)

# Arithmetic operation:
print("Addition: ", x+y)
print("Subtraction: ", x-y)
print("Multiplecation: ", x*y)
print("Division: ", x/y)
print("Floor Division: ", x//y)
print("modulo: ", x%y)
print("Power: ", x**(1/y))

# Comparision operation:
print("Equality: ", x==y)
print("Greater than: ", x>y)
print("Less than: ", x<y)
print("Not equal: ", x!=y)
print("Greater than equal: ", x>=y)
print("Less than equal: ", x<=y)

)";
    PyRun_SimpleString(pythonCode);
    Py_Finalize();
}