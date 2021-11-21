.PHONY:	compile	link	run	all
.SILENT:
compile:
	g++ -o main.o -c main.cpp

link:
	g++ -o MAIN main.o -L./libs/xerces-c-3.2.3/src -lxerces-c

run:
	./MAIN

all:
	g++ -o main.o -c main.cpp && \
	g++ -o MAIN main.o -L./libs/xerces-c-3.2.3/src -lxerces-c && \
	./MAIN
