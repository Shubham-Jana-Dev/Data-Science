#include <iostream>
#include <vector>
class statisics{
private:
    std::vector<int> dataSet;
public:
    statisics() : dataSet({ }){}
    statisics(std::vector <int> array) : dataSet(std::move(array)) {}
    std::vector <int> createArray(){
        int arraySize = 0;
        std::cout << "Enter the size of the data set: ";
        std::cin >> arraySize;
        for(int i = 0; i<arraySize; i++){
            int element = 0;
            std::cout << "Enter the element: ";
            std::cin >> element;
            dataSet.push_back(element);
        }
        return dataSet;
    }
    std::vector <int> sortData(){
        createArray();
            int temp = 0;
            for(int i = 0; i < dataSet.size(); i++){
                for (int j = i+1; j < dataSet.size(); j++){
                    if(dataSet[i]>dataSet[j]){
                        temp = dataSet[i];
                        dataSet[i] = dataSet[j];
                        dataSet[j] = temp;
                    }
                }
            }
            return dataSet;
    }
    double median_cal(){
        sortData();
        if(dataSet.empty()){
            return 0;
        }
        else if((dataSet.size())%2 != 0){
            int midile = (dataSet.size())/2;
            std::cout << "The midile element of the data set is: " << dataSet[midile] << std::endl;
            return dataSet[midile];
        }else{
            int midile = (dataSet.size())/2;
            std::cout << "The midile elements of the data set are: " << dataSet[midile-1] << " and "<<dataSet[midile] << std::endl;
            return (dataSet[midile - 1] + dataSet[midile])/2.0; 
        }
    }
    void displayArray(){
        std::cout << "[";
        bool first = true;
        for (int j : dataSet){
            if(first){
                std::cout << j ;
                first = false;
            }else{
                std::cout << ", " << j;
            }
        }
        std::cout<< "]" <<std::endl;
    }

};
int main(){
    statisics s1;
    double median = s1.median_cal();
    std::cout << "data set ";
    s1.displayArray();
    std::cout << " the median " << median << std::endl;
    return 0;
}