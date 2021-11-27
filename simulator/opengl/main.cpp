#include <GLFW/glfw3.h>

#include <iostream>


const unsigned int WINDOW_WIDTH = 1440;
const unsigned int WINDOW_HEIGHT = 810;

void keyHandler(GLFWwindow*, int, int, int, int);


int main()
{
    std::cout << "start." << std::endl;

    // TODO

    // glfwInit();
    // glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    // glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 4);
    // glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    // glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);

    // GLFWwindow* window = glfwCreateWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "advent_gl", nullptr, nullptr);

    // if (!window)
    // {
    //     std::cerr << "Failed to create window." << std::endl;
    //     glfwTerminate();
    //     return -1;
    // }

    // glfwMakeContextCurrent(window);
    // glfwSetKeyCallback(window, keyHandler);

    // glfwTerminate();

    return 0;
}
