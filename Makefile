.PHONY: build
build:
	g++ -O3 -o matrix_operations matrix_operations.cpp

.PHONY: all
all:
	g++ -O3 -fpic -c ./matrix_operations.cpp
	g++ -shared -o matrix_operations.so  ./matrix_operations.o
