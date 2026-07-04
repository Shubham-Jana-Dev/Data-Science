//
// g++ -std=c++17 argmax_argmin.cpp -o argmax_argmin.exe && argmax_argmin.exe
//
//
//  Created by Shubham Jana on 04/07/26.
//
#include <iostream>
#include <vector>

int argmax(const std::vector<int>& MyArray){
    int maxElement = INT_MIN;
    int argmax = 0;
    for (int i = 0; i < MyArray.size(); i++){
        if(MyArray[i] > maxElement){
            maxElement = MyArray[i];
            argmax = i;
        }
    }
    return argmax;
}

int argmin(const std::vector<int>& TheArray){
    int min_element = INT_MAX;
    int index = 0;
    for(int j = 0; j < TheArray.size();j++){
        if(min_element > TheArray[j]){
            min_element = TheArray[j];
            index = j;
        }
    }
    return index;
}
int main(){
    std::vector <int> theArray = {34,45,76,11,98,90,21};
    int argma = argmax(theArray);
    std::cout << "The position of the maximum element is: " << argma << std::endl;
    int argmi = argmin(theArray);
    std::cout << "The position of the minimum element is: " << argmi << std::endl;
    return 0;
}
