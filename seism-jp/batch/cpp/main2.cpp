#include "hello.hpp"
#include "greet.hpp"

// compile. -> create hello.o, main2.o
//  g++ -c main2.cpp hello.cpp

// link. -> create a.out
// g++ -o a.out main2.o hello.o

// exec.
// /a.out

int main() {
    hello();
    greet();
}
