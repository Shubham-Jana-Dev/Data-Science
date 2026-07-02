//
// g++ -std=c++17 mean.cpp -o mean.exe && ./mean.exe
//  
//
//  Created by Shubham Jana on 02/07/26.
//
#include <iostream>
#include <vector>
class get_array{
protected:
    std::vector <int> array_creation(){
        int aSize = 0;
        std::vector <int> theArray = { };
        std::cout << "Enter the size of the array: ";
        std::cin >> aSize;
        for (int i = 0; i < aSize; i++){
            int element = 0;
            std::cout << "Enter the element: ";
            std::cin >> element;
            theArray.push_back(element);
        }
        return theArray;
    }
};
class statistics : public get_array{
public:
    double mean_calculation(){
        std::vector <int> myArray = array_creation();
        if(myArray.empty()){
            return 0;
        }
        int totalNumberOfElement = myArray.size();
        double elementSum = 0;
        for ( int j : myArray){
            elementSum = elementSum + j;
        }
        return elementSum/totalNumberOfElement;
    }
};
int main(){
    statistics s1;
    float mean = s1.mean_calculation();
    std::cout<< "The mean of your given data set is " << mean << std::endl;
    return 0;
}
