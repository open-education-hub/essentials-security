BINARY = ../public/plain

all:
	rm -rf ../public/plain
	python3 generate_c_file.py
	gcc -o $(BINARY) plain.c

.PHONY: all
