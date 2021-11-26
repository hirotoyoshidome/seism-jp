.PHONY:	compile	link	build

.SILENT:
compile:
	g++ -std=c++11 -c MyFrame.cpp MyApp.cpp `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`

link:
	g++ -o ./MAIN MyApp.o MyFrame.o `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`

build:
	g++ -std=c++11 -c MyFrame.cpp MyApp.cpp `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs` && \
	g++ -o ./MAIN MyApp.o MyFrame.o `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`

clean:
	rm -f *.o
