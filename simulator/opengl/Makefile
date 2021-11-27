.PHONY:	compile	link	clear

.SILENT:
compile:
	g++ -g -Wall -std=c++11 -o main.o -c main.cpp -I ./libs/glfw-3.3.5/include

link:
	g++ -g -Wall -o MAIN main.o -L ./libs/glfw-3.3.5/build/src -lglfw3

clear:
	rm -f *.o
