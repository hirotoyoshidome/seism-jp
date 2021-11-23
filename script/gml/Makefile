.PHONY:	compile	link	run	all	clean
.SILENT:
compile:
	g++ -c main.cpp SampleSaxHandler.cpp

link:
	g++ -o MAIN main.o SampleSaxHandler.o -L./libs/xerces-c-3.2.3/src -lxerces-c

run:
	./MAIN

build:
	g++ -c main.cpp SampleSaxHandler.cpp && \
	g++ -o MAIN main.o SampleSaxHandler.o -L./libs/xerces-c-3.2.3/src -lxerces-c

clean:
	rm -f *.o
