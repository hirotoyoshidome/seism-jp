# version
cmake_minimum_required(VERSION 3.9)
# project
project(test_cmake CXX)

# link
# add_executable(a.out main2.cpp hello.cpp)

# static lib.
add_library(greetings STATIC hello.cpp greet.cpp)
# compile
add_executable(a.out main2.cpp)
# link
target_link_libraries(a.out greetings)
