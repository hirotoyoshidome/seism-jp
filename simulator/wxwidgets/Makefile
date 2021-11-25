.PHONY:	compile	link	build

.SILENT:
compile:
	g++ -c main.cpp app.cpp `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`

link:
	g++ app.o `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`

build:
	g++ -c main.cpp `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs` && \
	g++ -o MAIN main.o `./libs/wxWidgets-3.1.5/gtk-build/wx-config --cxxflags --libs`
