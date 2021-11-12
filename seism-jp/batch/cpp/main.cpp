#include <fstream>
#include <iostream>
#include <string>

// g++ -o main main.cpp


int main() {
    // std::cout << "Hello!" << std::endl;
    std::ifstream ifs("./sample.txt");
    int buf_size = 256;

    char str[buf_size];
    std::string str2;

    if (ifs.fail()) {
        std::cerr << "Failed to open file." << std::endl;
        return -1;
    }

    // while (ifs.getline(str, buf_size)) {
    //     std::cout << str << std::endl;
    // }

    while (getline(ifs, str2)) {
        std::cout << str2 << std::endl;
    }

    return 0;
}
