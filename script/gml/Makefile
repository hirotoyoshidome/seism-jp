.PHONY:	compile	link	build	clean
.SILENT:
compile:
	g++ -std=c++11 -c main.cpp SampleSaxHandler.cpp

link:
	g++ -o MAIN main.o SampleSaxHandler.o -L./libs/xerces-c-3.2.3/src -lxerces-c

build:
	g++ -c main.cpp SampleSaxHandler.cpp && \
	g++ -o MAIN main.o SampleSaxHandler.o -L./libs/xerces-c-3.2.3/src -lxerces-c

clean:
	rm -f *.o
