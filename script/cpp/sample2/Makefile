.PHONY:	compile	link	run	clean

.SILENT:
compile:
	g++ -o main.o -c main.cpp -I ../libs/eigen-3.4.0 -I ../libs/xerces-c-3.2.3

link:
	g++ -o MAIN main.o -L ../libs/xerces-c-3.2.3 -lxerces-c

run:
	./MAIN

clean:
	rm -f *.o
