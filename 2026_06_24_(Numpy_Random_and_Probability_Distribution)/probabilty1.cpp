//
//  probabilty1.cpp
//  
//
//  Created by Shubham Jana on 25/06/26.
//
#include <iostream>
#include <random>
int main(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> distrib(0.0, 1.0);
    std::cout << "Generating 5 random values for data scince simulation:"<<std::endl;
    std::cout << "-----------------------------------------------------------" <<std::endl;
    for (int i = 0; i < 5; ++i){
        double random_value = distrib(gen);
        std::cout << "Value " << i + 1 << ": " << random_value << std::endl;
    }
    return 0;
}
