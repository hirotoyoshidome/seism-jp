#include "hello.hpp"
#include "greet.hpp"

// compile. -> create hello.o, main.o
// g++ -c main.cpp hello.cpp greet.cpp

// link. -> create a.out
// g++ -o a.out main.o hello.o greet.cpp

// exec.
// /a.out

int main() {
    hello();
    greet();
}
