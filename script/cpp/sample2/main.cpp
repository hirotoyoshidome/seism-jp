#include <fstream>
#include <iostream>
#include <string>
using namespace std;

#include <Eigen/Dense>
using Eigen::MatrixXd;

#include <xercesc/dom/DOM.hpp>
#include <xercesc/dom/DOMElement.hpp>
#include <xercesc/dom/DOMNode.hpp>
#include <xercesc/dom/DOMText.hpp>
#include <xercesc/parsers/XercesDOMParser.hpp>
#include <xercesc/sax/HandlerBase.hpp>
using namespace xercesc;


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

    // use eigen.
    MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;

    return 0;
}
