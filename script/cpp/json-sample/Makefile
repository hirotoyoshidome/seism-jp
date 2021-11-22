.PHONY:	compile	link	run	all	clean
.SILENT:
compile:
	g++ -std=c++11 -o main.o -c main.cpp -I../libs/single_include

link:
	g++ -o MAIN main.o

run:
	./MAIN

all:
	g++ -std=c++11 -o main.o -c main.cpp -I../libs/single_include && \
	g++ -o MAIN main.o && \
	./MAIN

clean:
	rm -f *.o
